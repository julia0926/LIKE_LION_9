from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm # 로그인, 회원가입 폼 
from .forms import RegisterForm
#회원가입 
def signup(request):
    if request.method == 'POST': #Post 방식 
        form = RegisterForm(request.POST)
        if form.is_valid(): #유효성 검사 
            user = form.save()
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'account/signup.html', {'form':form})
    else: #get 방식 
        form = RegisterForm()
        return render(request, 'account/signup.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'account/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'account/login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('main')