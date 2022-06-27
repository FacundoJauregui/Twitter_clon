from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Profile, Post, Relationship
from .forms import UserRegisterForm, PostForm, UserEditForm, ProfileEditForm
from django.contrib.auth.models import User
from django .contrib.auth.decorators import login_required
import random


@login_required
def primeraVista(request):
    
    posts = Post.objects.all()
    
    if request.method == 'POST':
        
        form = PostForm(request.POST)
        
        if form.is_valid():
            
            post = form.save(commit = False)
            post.user = request.user
            post.save()
            return redirect('Home')
        
    else:
        form = PostForm()
    
    users = User.objects.all()
    profiles = []
    if len(users) > 0:
        while len(profiles) !=3:
            user = random.choice(users)
            if user != request.user and user not in profiles:
                profiles.append(user)
    
    context = {'posts' : posts, 'form':form, 'profiles':profiles}
    
    return render(request, 'inicio.html', context)



def register(request):
    
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            aux = form.save()
            profile = Profile()
            profile.user = aux
            profile.save()
            request.user = aux
            return redirect('Home')
        
    else:
        form = UserRegisterForm()
        
    context = {'form':form}
    
    return render(request,'register.html', context)

def deletePost(request, post_id):
    
    post = Post.objects.get(id = post_id)
    post.delete()
    
    return redirect('Home')


def profile(request, username):
    
    user = User.objects.get(username = username)
    posts = user.post.all()
    context = {'user':user, 'posts': posts}
    print(user.id)
    
    return render(request, 'profile.html', context)

def edit_profile(request):
    user = request.user
     
    if request.method == 'POST':
        
        u_form = UserEditForm(request.POST, instance = user)
        p_form = ProfileEditForm(request.POST, request.FILES, instance = user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            
            u_form.cleaned_data
            
            user.password1 = u_form['password1']
            user.password2 = u_form['password2']
            
            u_form.save()
            p_form.save()
            
            return redirect ('Home')
            
    else:
        u_form = UserEditForm(instance = request.user)
        p_form = ProfileEditForm()
    
    context = {'u_form':u_form, 'p_form':p_form}
    
    return render(request, 'editProfile.html', context)

def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username = username)
    to_user_id = to_user
    rel = Relationship(from_user = current_user, to_user = to_user_id)
    rel.save()
    
    return redirect('Home')

def unfollow(request, username):
    
    current_user = request.user
    to_user = User.objects.get(username = username)
    to_user_id = to_user.id
    rel = Relationship.objects.get(from_user = current_user.id, to_user = to_user_id)
    rel.delete()
    
    return redirect('Home')
    