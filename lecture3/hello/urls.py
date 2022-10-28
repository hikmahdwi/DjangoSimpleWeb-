from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hikmah", views.hikmah, name="hikmah"),
    path("dear", views.dear, name="dear"),
    path("<str:name>", views.greet, name="greet")
]