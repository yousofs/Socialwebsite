from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserLoginForm, UserRegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from posts.models import Post
from django.contrib.auth.decorators import login_required


def user_login(request):
    next = request.GET.get('next')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You logged in successfully', 'success')
                if next:
                    return redirect(next)
                return redirect('posts:all_posts')
            else:
                messages.error(request, 'Wrong username or password', 'warning')
    else:
        form = UserLoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            login(request, user)
            messages.success(request, 'You registered successfully!', 'success')
            return redirect('posts:all_posts')

    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You logged out successfully', 'success')
    return redirect('posts:all_posts')


@login_required
def user_dashboard(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(user=user).order_by('-created')
    self_dash = False
    if request.user.id == user_id:
        self_dash = True
    return render(request, 'account/dashboard.html', {
        'user': user,
        'posts': posts,
        'self_dash': self_dash
    })


@login_required()
def edit_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user.profile)
        if form.is_valid():
            form.save()
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.username = form.cleaned_data['username']
            user.save()
            messages.success(request, 'Your profile edited successfully', 'success')
            redirect('account:dashboard', user_id)
    else:
        form = EditProfileForm(instance=user.profile, initial={
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'username': request.user.username,
        })
    return render(request, 'account/edit_profile.html', {'form': form})
