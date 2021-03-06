"""marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from app import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/all/', views.list_all),
    path('app/cadastrar/', views.cadastro),
    path('app/detail/<id_produto>/', views.app_detail),
    path('app/inativar/<id_produto>/', views.inativar),
    path('app/cadastrar/submit/', views.set_produto),
    path('app/alterar/<int:id_produto>/', views.alterar),
    path('app/alterar/<int:id_produto>/submit/', views.update_produto),
    path('app/all/submit/', views.consulta_produto),
    path('login/', views.login_user),
    path('login/submit/', views.submit_login),
    path('app/register/', views.register),
    path('app/register/submit/', views.set_vendedor),
    path('', views.index),
    path('logout/', views.logout_user)
]