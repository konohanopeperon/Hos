from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            messages.error(request, 'ユーザーIDまたはパスワードが正しくありません。')
    return render(request, 'Kadai1/L100/Login.html')

def menu_view(request):
    return render(request, 'Kadai1/L100/Menu.html')


def login(request):
    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    return redirect('Kadai1/L100/Login.html')
