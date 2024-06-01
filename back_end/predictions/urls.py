from django.urls import path
from . import views

urlpatterns = [
    path("", views.predictions, name="predictions"),
    path("predictions_result/<int:team_id>/<int:vs_team_id>/", views.predictionsResult, name="predictions_result"),

]
