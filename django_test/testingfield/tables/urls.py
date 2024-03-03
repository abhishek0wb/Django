from django.urls import path

from tables import views

urlpatterns = [
    path("", views.tabs, name="index"),
    path("about/", views.about, name="index"),
    path("contact/", views.contact, name="index")
]