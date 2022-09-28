from http.client import HTTPResponse
from django.shortcuts import render



def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {"tasks": request.session["tasks"]})

from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import NewTaskForm

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            new_task = form.cleaned_data["task"]
            priority = form.cleaned_data["priority"]
            new_task = f'{new_task}@{priority}'
            if new_task not in request.session["tasks"]:
                request.session["tasks"] += [new_task]
                return HttpResponseRedirect(reverse("tasks:index"))
            else:
                return render(request, "tasks/add.html", {"form": form, "errormsg": "Task names must be unique"})
        else:
            return render(request, "tasks/add.html", {"form": form})
    else:
        return render(request, "tasks/add.html", {"form": NewTaskForm()})