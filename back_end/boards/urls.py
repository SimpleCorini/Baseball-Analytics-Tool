from django.urls import path
from . import views

urlpatterns = [
    path("article_list", views.article_list, name='article_list'),
    path("article_create", views.article_create, name='article_create'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
]
