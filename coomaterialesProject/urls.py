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
    path('create/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    # path('userList/',views.userListView.as_view()),
    # path('userEdit/<int:pk>/',views.userEditView.as_view()),
    # path('userDelete/<int:pk>/',views.userDeleteView.as_view()),
    # path('productoCreate/',views.ProductoCreateView.as_view()),
    # path('productoList/',views.productoListView.as_view()),
    # path('productoEdit/<int:pk>/',views.productoEditView.as_view()),
    # path('productoDelete/<int:pk>/',views.productoDeleteView.as_view()),
    # path('proveedorCreate/',views.ProveedorCreateView.as_view()),
    # path('proveedorList/',views.proveedorListView.as_view()),
    # path('proveedorEdit/<int:pk>/',views.proveedorEditView.as_view()),
    # path('proveedorDelete/<int:pk>/',views.proveedorDeleteView.as_view()),
    # path('fabricanteCreate/',views.FabricanteCreateView.as_view()),
    # path('fabricanteList/',views.fabricanteListView.as_view()),
    # path('fabricanteEdit/<int:pk>/',views.fabricanteEditView.as_view()),
    # path('fabricanteDelete/<int:pk>/',views.fabricanteDeleteView.as_view()),
    path('categoriaCreate/',views.CategoriaCreateView.as_view()),
    # path('categoriaList/',views.categoriaListView.as_view()),
    # path('categoriaEdit/<int:pk>/',views.categoriaEditView.as_view()),
    # path('categoriaDelete/<int:pk>/',views.categoriaDeleteView.as_view()),
    path('refresh/', TokenRefreshView.as_view())

]
