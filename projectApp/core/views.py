# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from projectApp.core.models import ProjectList, Item
from projectApp.core.forms import SignUpForm, CreateListForm


def index(request, id):
    ls = ProjectList.objects.get(id=id)
    if ls in request.user.todolist.all():
        if request.method == "POST":
            if request.POST.get("save"):
                print("save!!")
                for item in ls.item_set.all():
                    if request.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            if request.POST.get("delete"):
                print("delete!!")
                for item in ls.item_set.all():
                    if request.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                        item.delete()
                    else:
                        item.complete = False
            elif request.POST.get("deleteProj"):
                ls.delete()
                return render(request, "dashboard.html", {})
            elif request.POST.get("add"):
                newItem = request.POST.get("new")
                for tab in ls.tabs_set.all():
                    tab.active = False
                    if request.POST.get("currentTab") == tab.name:
                        print("current tab")
                        tab.active = True
                        print(tab)
                        if newItem != "":
                            ls.item_set.create(text=newItem, complete=False, tab=tab)
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


def dashboard(response):
    return render(response, "dashboard.html", {})


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
