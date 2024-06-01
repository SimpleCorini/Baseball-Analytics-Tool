from django.urls import path
from . import views

urlpatterns = [
    path("", views.analysis, name="analysis"),
    path("<int:id>/", views.analysisTeam, name="analysis_team"),
]
