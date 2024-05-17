from django.shortcuts import render,redirect
from .forms import RegistrationForm, LoginForm 
from django.contrib.auth import authenticate, login as auth_login

def about(request):
    return render(request, 'account/about.html')

def signin(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        
    else:
        form = RegistrationForm()
        
    return render(request, 'account/signin.html', {
        'form': form
    })

def login(request) :
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)
                return redirect('/')
            
            else:
                form = LoginForm()
    else:
        form =LoginForm()
        
    return render(request, 'account/login.html', {
        'form': form
    })
                
