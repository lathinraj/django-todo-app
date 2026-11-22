"""
URL configuration for todoApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(),name="home"),
    path('todolist',TodoListView.as_view(),name='list'),
    path('addtodo',AddTodoView.as_view(),name='add'),
    path('deletetodo/<int:id>',DeleteTodoView.as_view(),name="delete"),
    path('edittodo/<int:id>',EditTodoView.as_view(),name="edit"),
    path('status/<int:id>',UpdateStatusView.as_view(),name='status')
]
