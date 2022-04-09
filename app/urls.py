from tkinter import N
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path('deleteTodo/<int:id>/', views.deleteTodo, name='deleteTodo'),
    path('editTodo/<int:id>/', views.editTodo, name='editTodo'),
]

