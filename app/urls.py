"""
URL configuration for app project.

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
from django.urls import path
from .views import create_list, delete_list, get_list, update_list

urlpatterns = [
    path('list/create', create_list, name='create-list'),
    path('list/get_all', get_list, name='get-list'),
    path('list/update/<str:id>', update_list, name='update-list'),
    path('list/delete/<str:id>', delete_list, name='delete-list'),
]
