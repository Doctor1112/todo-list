from django.contrib import admin
from django.urls import path, include
from .views import complete, LoginView, logout_user, create_todo, edit, todo_list, RegisterUserView, \
    delete, add_description, edit_description
urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('todo/<int:pk>', todo_list, name='detail'),
    path("complete/<int:pk>", complete, name="complete"),
    path("register/", RegisterUserView.as_view(), name='register'),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("logout/", logout_user, name='logout'),
    path("create/", create_todo, name="create"),
    path("create/<int:pk>", create_todo, name="create"),
    path("edit/<int:pk>", edit, name="edit"),
    path("delete/<int:pk>", delete, name="delete"),
    path("add_desc/<int:pk>", add_description, name="add_desc"),
    path("edit_desc/<int:pk>", edit_description, name="edit_desc"),

]