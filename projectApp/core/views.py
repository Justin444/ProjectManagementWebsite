# Create your views here.
from datetime import datetime
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from projectApp.core.models import ProjectList, Item, User
from projectApp.core.forms import SignUpForm, CreateListForm,DateForm


def index(request, id):
    ls = ProjectList.objects.get(id=id)
    if ls in request.user.todolist.all():
        if request.method == "POST":
            if request.POST.get("save"):
                print("save!!")
                for tab in ls.tabs_set.all():
                    for item in tab.item_set.all():
                        if request.POST.get("c" + str(item.id)) == "clicked":
                            item.complete = True
                        else:
                            item.complete = False
                        item.save()
            elif request.POST.get("delete"):
                print("delete!!")
                for tab in ls.tabs_set.all():
                    for item in tab.item_set.all():
                        if request.POST.get("c" + str(item.id)) == "clicked":
                            item.complete = True
                            item.delete()
                        else:
                            item.complete = False
            elif request.POST.get("renameTab"):
                r = request.POST.get("renameTab")
                print('renametab')
                for tab in ls.tabs_set.all():
                    if request.POST.get("currentTab") == tab.name:
                        print(request.POST.get("currentTab"))
                        tab.name = r
                        tab.save()
                    else:
                        print('invalid')
            elif request.POST.get("deleteTab"):
                for tab in ls.tabs_set.all():
                    if request.POST.get("currentTab") == tab.name:
                        tab.delete()
                    else:
                        print('invalid')
            elif request.POST.get("deleteProj"):
                ls.delete()
                return render(request, "dashboard.html", {})
            elif request.POST.get("add"):
                newItem = request.POST.get("new")
                dueDate = request.POST.get("duedate")
                for tab in ls.tabs_set.all():
                    if request.POST.get("currentTab") == tab.name:
                        print("current tab")
                        print(dueDate)
                        if newItem != "" and dueDate != "":
                            tab.item_set.create(text=newItem, complete=False, due_date=dueDate)
                        elif newItem != "":
                            tab.item_set.create(text=newItem, complete=False)
                        else:
                            print("invalid")
            elif request.POST.get("addTab"):
                newTab = request.POST.get("newtab")
                if newTab != "":
                    ls.tabs_set.create(name=newTab)
                else:
                    print("invalid tab")

    return render(request, "index.html", {"ls": ls})


def create(response):
    if response.method == "POST":
        print('post')
        form = CreateListForm(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            p = ProjectList(name=n)
            p.save()
            response.user.todolist.add(p)
            return HttpResponseRedirect("/%i" %p.id)
    else:
        form = CreateListForm()

    return render(response, 'create.html', {"form":form})


def dashboard(request):
    if request.method == "POST":
        print('post')
        if request.POST.get("addproj"):
            name = request.POST.get("addproj")
            p = ProjectList(name=name)
            p.save()
            request.user.todolist.add(p)
            return HttpResponseRedirect("/%i" %p.id)
        elif request.POST.get("rename"):
            prename = request.POST.getlist('currentProjRename')
            rename = request.POST.get("rename")
            ls = ProjectList.objects.get(id=prename[0])
            if ls in request.user.todolist.all():
                ls.name = rename
                ls.save()
        elif request.POST.get("shareProj"):
            sp = request.POST.get('shareProj').split(',')
            print(sp)
            uname = request.POST.get("uname")
            user = User.objects.get(username__iexact=uname)
            ls = ProjectList.objects.get(id=sp[1])
            print(user)
            print('match')
            ls.shareduser.add(user)

    return render(request, "dashboard.html", {})


def home(response):
    return render(response, 'home.html', {})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
