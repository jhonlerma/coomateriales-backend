from django.contrib import admin
from authApp import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from django.urls import path


urlpatterns = [
    path('userCreate/',views.userCreateView.as_view()),
    path('userList/',views.userListView.as_view()),
    path('userEdit/',views.userEditView.as_view()),
    path('userDelete/',views.userDeleteView.as_view()),
    path('productoCreate/',views.productoCreateView.as_view()),
    path('productoList/',views.productoListView.as_view()),
    path('productoEdit/',views.productoEditView.as_view()),
    path('productoDelete/',views.productoDeleteView.as_view()),
    path('proveedorCreate/',views.proveedorCreateView.as_view()),
    path('proveedorList/',views.proveedorListView.as_view()),
    path('proveedorEdit/',views.proveedorEditView.as_view()),
    path('proveedorDelete/',views.proveedorDeleteView.as_view()),
    path('fabricanteCreate/',views.fabricanteCreateView.as_view()),
    path('fabricanteList/',views.fabricanteListView.as_view()),
    path('fabricanteEdit/',views.fabricanteEditView.as_view()),
    path('fabricanteDelete/',views.fabricanteDeleteView.as_view()),
    path('categoriaCreate/',views.categoriaCreateView.as_view()),
    path('categoriaList/',views.categoriaListView.as_view()),
    path('categoriaEdit/',views.categoriaEditView.as_view()),
    path('categoriaDelete/',views.categoriaDeleteView.as_view()),
    path('categoriaDelete/',views.categoriaCreateView.as_view()),
    path('refresh/',TokenRefreshView.as_view)
]