# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from projectApp.core.models import ProjectList, Item
from projectApp.core.forms import SignUpForm, CreateListForm


def index(response, id):
    ls = ProjectList.objects.get(id=id)

    if ls in response.user.todolist.all():

        if response.method == "POST":
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")

        return render(response, "index.html", {"ls": ls})

    return render(response, "home.html", {})


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
