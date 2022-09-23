from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    isClasstoday = now.weekday() == 1 or now.weekday() == 3
    s = "YES" if isClasstoday else "NO"
    context = {
        "classtoday": isClasstoday,
        "now": now,
    }
    return render(request, "classtoday/mainpage.html", context)
