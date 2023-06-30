from django.urls import path
from . import views

urlpatterns = [
    # photo
    path('photo', views.photo_album, name="photoAlbum"),
    path('photo/create', views.photo_create, name='photo_create'),

    # auth
    path('', views.loginUser, name="loginpage"),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='registerpage'),

    # category
    path('category/', views.category, name="category"),
]
