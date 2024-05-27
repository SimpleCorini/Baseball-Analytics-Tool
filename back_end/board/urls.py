from django.urls import path
from . import views

urlpatterns = [
    path("analysis", views.analysis, name='analysis'),
    path("analysis_DOOSAN", views.analysis_DOOSAN, name='analysis_DOOSAN'),
    path("analysis_HANHWA", views.analysis_HANHWA, name='analysis_HANHWA'),
    path("analysis_KIA", views.analysis_KIA, name='analysis_KIA'),
    path("analysis_KIWOOM", views.analysis_KIWOOM, name='analysis_KIWOOM'),
    path("analysis_KT", views.analysis_KT, name='analysis_KT'),
    path("analysis_LG", views.analysis_LG, name='analysis_LG'),
    path("analysis_LOTTE", views.analysis_LOTTE, name='analysis_LOTTE'),
    path("analysis_NC", views.analysis_NC, name='analysis_NC'),
    path("analysis_SAMSUNG", views.analysis_SAMSUNG, name='analysis_SAMSUNG'),
    path("analysis_SSG", views.analysis_SSG, name='analysis_SSG'), 
    path("analysis_result", views.analysis_result, name='analysis_result'),

    path("predictions", views.predictions, name='predictions'),
    path("predictions_result", views.predictions_result, name='predictions_result'),

    path("matchups", views.matchups, name='matchups'),
    path("matchups_result", views.matchups_result, name='matchups_result'),

    path("article_list", views.article_list, name='article_list'),
    path("article_create", views.article_create, name='article_create'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
]
