from django.urls import path
from . import views

urlpatterns = [
    path("article_list", views.article_list, name='article_list'),
    path("article_create", views.article_create, name='article_create'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/<int:pk>/edit/', views.edit_article, name='edit_article'),
    path('comment/<int:pk>/delete/', views.delete_article, name='delete_article'),
    path('article/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('toggle_like/<str:content_type>/<int:object_id>/', views.toggle_like, name='toggle_like'),
]
