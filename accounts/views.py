from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout


def sign_up_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('accounts:login')
    else:
        user_form = UserCreationForm()
    return render(request, 'accounts/sign_up.html', {'user_form': user_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cria_lista:index')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm(request.POST)
    return render(request, 'accounts/login.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('cria_lista:index')
