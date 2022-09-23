from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
tasks = ['foo', 'bar', 'bazingo', 'fun']

def index(request):
    return render(request, "tasks/index.html", {"tasks": tasks})

from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import NewTaskForm

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            new_task = form.cleaned_data["task"]
            priority = form.cleaned_data["priority"]
            tasks.append(f'{new_task}@{priority}')
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {"form": form, "errormsg":"String too short"})
    else:
        return render(request, "tasks/add.html", {"form": NewTaskForm()})