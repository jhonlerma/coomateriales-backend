"""coomateriales_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from coomaterialesApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

    # USER PATHS
    path('user/create/', views.UserCreateView.as_view()),
    path('user/read/<int:pk>/', views.UserDetailView.as_view()),
    path('user/update/',views.userEditView.as_view()),
    path('user/delete/', views.UserDeleteView.as_view()),
    path('user/list/',views.userListView.as_view()),

    # CATEGORIA PATHS
    path('categoria/create/', views.UserCreateView.as_view()),
    path('categoria/read/<int:pk>/', views.UserDetailView.as_view()),
    path('categoria/update/',views.userEditView.as_view()),
    path('categoria/delete/', views.UserDeleteView.as_view()),
    path('categoria/list/',views.userListView.as_view()),

    # FABRICANTE PATHS
    path('fabricante/create/', views.UserCreateView.as_view()),
    path('fabricante/read/<int:pk>/', views.UserDetailView.as_view()),
    path('fabricante/update/',views.userEditView.as_view()),
    path('fabricante/delete/', views.UserDeleteView.as_view()),
    path('fabricante/list/',views.userListView.as_view()),

    # PROVEEDOR PATHS
    path('proveedor/create/', views.UserCreateView.as_view()),
    path('proveedor/read/<int:pk>/', views.UserDetailView.as_view()),
    path('proveedor/update/',views.userEditView.as_view()),
    path('proveedor/delete/', views.UserDeleteView.as_view()),
    path('proveedor/list/',views.userListView.as_view()),

    # PRODUCTO PATHS
    path('producto/create/', views.UserCreateView.as_view()),
    path('producto/read/<int:pk>/', views.UserDetailView.as_view()),
    path('producto/update/',views.userEditView.as_view()),
    path('producto/delete/', views.UserDeleteView.as_view()),
    path('producto/list/',views.userListView.as_view()),

]
