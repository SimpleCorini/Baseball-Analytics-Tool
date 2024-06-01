from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("logout", views.logout_view, name="logout"),
    path("profile_create", views.set_profile, name="profile_create"),
    path("profile_update", views.update_profile, name="profile_update"),
]
