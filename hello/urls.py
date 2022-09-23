from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("class", views.uaa490, name="uaa490"),
    path("<str:name>", views.greet, name="greet"),
]
