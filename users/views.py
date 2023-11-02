from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm, ChangeUserForm, ChangePasswordForm
from django.contrib import auth, messages
from products.models import Product

# Create your views here.

# Главная страница
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'title_page': 'Главная', 'products': products})


# Авторизация
def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    context = {'form': form, 'title_page': 'Войти'}
    return render(request, 'sign_in.html', context)


# Регистрация
def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            auth.login(request, new_user)
            return redirect('index')
    else:
        form = RegistrationForm()
    context = {'form': form, 'title_page': 'Регистрация'}
    return render(request, 'sign_up.html', context)


# Выход из аккаунта
@login_required
def logout(request):
    auth.logout(request)
    return redirect('index')


# Профиль и возможность его изменять
@login_required
def profile(request):
    if request.method == 'POST':
        form = ChangeUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ChangeUserForm(instance=request.user)
    context = {'form': form,
               'user': request.user,
               'title_page': 'Профиль'}
    return render(request, 'profile.html', context)


# Изменить пароль
@login_required
def change_password(request):
    try:
        if request.method == 'POST':
            form = ChangePasswordForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                auth.update_session_auth_hash(request, user)
                messages.success(request, 'Вы успешно изменили пароль')
                return redirect('index')

        else:
            form = ChangePasswordForm(request.user)
    except:
        pass
        # return redirect(request.META.get('HTTP_REFERER'))

    context = {'form': form, 'title_page': 'Изменить пароль'}
    return render(request, 'change_password.html', context)



