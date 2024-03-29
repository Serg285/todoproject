"""
URL configuration for todoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from todoapp.views import todoappView, addTodoView, deleteTodoView
from backupapp.views import backupView, addBackupView,addBackupViewADSUMS, home, password1
from generator.views import password
from vckpapp.views import vckp_users

urlpatterns = [
    path('', home, name = 'home'),
    path("admin/", admin.site.urls),
    path('todoapp/', todoappView, name = 'todoapp'),
    path('addTodoItem/',addTodoView),
    path('deleteTodoItem/<int:i>/', deleteTodoView),
    path('backupapp/', backupView, name = 'backupView'),
    path('addBackupItem/',addBackupView),
    path('addBackupItemADSUMS/', addBackupViewADSUMS),
    path('generator/', password1, name = 'password1'),
    path('gen_result/', password, name = 'password'),
    path('VckpAppUsers/',vckp_users , name = 'vckpappusers'),
]
