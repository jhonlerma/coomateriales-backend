"""coomaterialesProject URL Configuration

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
from coomaterialesApp import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

    # USER PATHS
    path('user/create/', views.UserCreateView.as_view()),
    path('user/read/<int:pk>/', views.UserDetailView.as_view()),
    path('user/update/',views.UserEditView.as_view()),
    path('user/delete/<int:pk>/', views.UserDeleteView.as_view()),
    path('user/list/',views.UserListView.as_view()),

    # CATEGORIA PATHS
    path('categoria/create/', views.CategoriaCreateView.as_view()),
    path('categoria/read/<int:pk>/', views.CategoriaDetailView.as_view()),
    path('categoria/update/',views.CategoriaEditView.as_view()),
    path('categoria/delete/<int:pk>/', views.CategoriaDeleteView.as_view()),
    path('categoria/list/',views.CategoriaListView.as_view()),

    # FABRICANTE PATHS
    path('fabricante/create/', views.FabricanteCreateView.as_view()),
    path('fabricante/read/<int:pk>/', views.FabricanteDetailView.as_view()),
    path('fabricante/update/',views.FabricanteEditView.as_view()),
    path('fabricante/delete/<int:pk>/', views.FabricanteDeleteView.as_view()),
    path('fabricante/list/',views.FabricanteListView.as_view()),

    # PROVEEDOR PATHS
    path('proveedor/create/', views.ProveedorCreateView.as_view()),
    path('proveedor/read/<int:pk>/', views.ProveedorDetailView.as_view()),
    path('proveedor/update/',views.ProveedorEditView.as_view()),
    path('proveedor/delete/<int:pk>/', views.ProveedorDeleteView.as_view()),
    path('proveedor/list/',views.ProveedorListView.as_view()),

    # PRODUCTO PATHS
    path('producto/create/', views.ProductoCreateView.as_view()),
    path('producto/read/<int:pk>/', views.ProductoDetailView.as_view()),
    path('producto/update/',views.ProductoEditView.as_view()),
    path('producto/delete/<int:pk>/', views.ProductoDeleteView.as_view()),
    path('producto/list/',views.ProductoListView.as_view()),

]
