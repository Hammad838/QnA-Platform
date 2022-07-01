from http.client import ImproperConnectionState
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<str:id>/', views.post, name='post'),

    path('create-post/', views.createPost, name='create-post'),
    path('update-post/<str:id>/', views.updatePost, name='update-post'),
    path('delete-post/<str:id>/', views.deletePost, name='delete-post'),
]