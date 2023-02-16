from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

from funcs.validators import validate_email
from .models import CustomUser
from .forms import LoginForm, SignupForm

def sign_up_view(request):
    form = SignupForm(request.POST or None)
    context ={
        'form': form,
    }
    if form.is_valid():
        form.save()
        #CustomUser.objects.create(
        #    first_name=form.cleaned_data.get('first_name'),
        #    last_name=form.cleaned_data.get('last_name'),
        #    date_of_birth=form.cleaned_data.get('date_of_birth'),
        #    email=form.cleaned_data.get('email'),
        #    username=form.cleaned_data.get('username'),
        #    password=make_password(form.cleaned_data.get('password1')),
        #)
        return render(request, 'accounts/login.html', {'account_created': 'Successfully created', 'form': LoginForm()})
    return render(request, 'accounts/signup.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('pages:home')
    form = LoginForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        if validate_email(username):
            username = CustomUser.objects.get(email__iexact=username).username
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('pages:home')
        context['error'] = 'No user with this credintials'
    return render(request, 'accounts/login.html', context)

@login_required
def logout_view(request):  
    if request.POST:
        logout(request)
        return redirect('accounts:login')
    return render(request, 'accounts/logout.html', {})

@login_required
def profile_view(request):
    context = {
        'name': request.user.get_full_name(),
        'username': request.user.username,
        'email': request.user.email,
        'dob': request.user.date_of_birth,
        'submissions': request.user.submissions.all(),
        #'scores': request.user.scores.all,
    }
    return render(request, 'accounts/profile.html', context)