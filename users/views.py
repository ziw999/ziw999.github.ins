from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.views.generic import CreateView, UpdateView
from django.views.generic import TemplateView


from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password)
            if user:
                auth.login(request, user)
                messages.success(request, f'{username}, Вы вошли в аккаунт')
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserLoginForm()

    context = { 
            'title': "Авторизация",
            'form': form
        }

    return render(request, 'users/login.html', context)


def register(request):
   
    if request.method=='POST':
        form=UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            
            session_key=request.session.session_key
            
            user=form.instance
            auth.login(request, user)
            
            # if session_key:
            #     User.objects.filter(session_key=session_key).update(user=user)
            
            messages.success(request, f'{user.username}, Вы успешно зарегистрированы и вошли в аккаунт!')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form=UserRegistrationForm()
        
    context={
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'users/register.html', context)



@login_required
def profile(request):
    if request.method=='POST':
        form = ProfileForm(data=request.POST, instance = request.user, files = request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Профиль успешно обновлен!')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance = request.user)

    context = {
        'title': "Кабинет",
        'form': form
    }

    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    messages.success(request, f'{request.user.username}, Вы вышли из аккаунта.')
    auth.logout(request)
    return redirect(reverse('users:login'))
