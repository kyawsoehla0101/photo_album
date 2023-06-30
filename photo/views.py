from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth import authenticate, login, logout
from .forms import *

from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
# Create your views here.


# auth
def loginUser(request):
     page = 'login'
     if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']

          user = authenticate(request, username=username, password=password)

          if user is not None:
               login(request, user)
               return redirect('photoAlbum')
     return render(request, 'layout/login_register.html', {'page':page})

def logoutUser(request):
     logout(request)
     return redirect('loginpage')

def registerUser(request):
     page = 'register'
     form = CustomUserCreationForm()
     if request.method == 'POST':
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
               user = form.save(commit=False)
               user.save()
               user = authenticate(request, username=user.username, password=request.POST['password1'])
               if user is not None:
                    login(request, user)
                    return redirect('loginpage')

               
       
     context = {
          'form':form,
          'page':page
     }
     return render(request, 'layout/login_register.html', context)

# photo
@login_required(login_url='loginpage')
def photo_album(request):
     user = request.user
     category = request.GET.get('category')
     photos = Photo.objects.all()
     categories = Category.objects.all()
     
     if category == None:
          photos = Photo.objects.filter(category__user=user)
     else:
          photos = Photo.objects.filter(category__name=category)
     context = {
          'categories':categories,
          'photos':photos
     }
     return render(request, 'photo/photo_index.html', context)

@login_required(login_url='loginpage')
def photo_create(request):
     page = photo_create
     photos = Photo.objects.all()
     form = PhotoForm()
     if request.method == 'POST':
          form = PhotoForm(request.POST, request.FILES)
          if form.is_valid():
               form.save()
          return redirect('photoAlbum')
     context = {
          'page':page,
          'photos':photos,
          'form':form
     }
     return render(request, 'photo/photo.html', context)

@login_required(login_url='loginpage')
def category(request):
     form = CategoryForm()
     context = {
          'form':form
     }
     return render(request, 'layout/category.html', context)


# category
@login_required(login_url='loginpage')
def category(request):
    page = 'category_create'
    categories = Category.objects.all()
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('category')

    context = {
        'page':page,
        'categories':categories,
        'form':form

    }
    return render(request, 'layout/category.html', context)


     
    