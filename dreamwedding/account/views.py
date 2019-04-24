from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                response = HttpResponseRedirect('/')
                response.set_cookie('username', username, 800)
                return response
            else:
                return HttpResponse('Login Faild ! ')
        else:
            return HttpResponse('Form Data is Faild !')

    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'theme/login.html', {'login_form': login_form})

def user_logout(request):
    logout(request)
    response = HttpResponseRedirect('/login/')
    response.delete_cookie('username')
    return response

