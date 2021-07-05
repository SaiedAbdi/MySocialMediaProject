from posts.forms import EditPostForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Profile
from posts.models import Post
from django.contrib.auth.decorators import login_required
from random import randint

# Create your views here.

def user_login(request):
    next = request.GET.get('next')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You are Logged Successfully! ', 'success')
                if next:
                    return redirect(next)
                return redirect('posts:all_posts')
            else:
                messages.error(request, 'Wrong Username or Password!', 'warning')
    else:
        form = UserLoginForm()
    return render(request, 'account/login.html', {'form':form})

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'],cd['email'], cd['password'])
            login(request, user)
            messages.success(request, 'you registered successfully!')
            return redirect('posts:all_posts')
    else:
        form = UserRegistrationForm()
    return render(request,'account/register.html', {'form':form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Yoy logout successfully!', 'success')
    return redirect('posts:all_posts')

@login_required
def user_dashboard(request, user_id):
    user = get_object_or_404(User,id=user_id)
    posts = Post.objects.filter(user =user)
    self_dash = False
    if request.user.id == user_id:
        self_dash = True

    return render(request, 'account/dashboard.html', {'user':user, 'posts':posts, 'self_dash':self_dash})

@login_required
def edit_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form =EditProfileForm(request.POST, instance=user.profile)
        if form.is_valid():
            form.save()
            user.email = form.cleaned_data['email']
            user.save()
            messages.success(request, 'Your Profile Edited successfully','success')
            return redirect('account:dashboard' , user_id)
    else:
        form = EditProfileForm(instance=user.profile, initial={'email': request.user.email})
    return render (request, 'account/edit_profile.html', {'form':form})


























