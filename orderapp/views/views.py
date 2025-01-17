from django.shortcuts import render, redirect
from django.http import HttpResponse
from .. import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from ..models import *
from django.http import HttpRequest


@login_required
def index(request: HttpRequest):
    user = request.user
    t=Ticket.objects.filter()
    
    return render(request, 'index.html', {'tickets': t, 'user': user})


'''
Security
'''
def login_view(request):
    form = forms._AuthenticationForm()
    
    if request.method == 'POST':
        form = forms._AuthenticationForm(request.POST)
        print(form.cleansed_data)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse('Invalid Login')
    
    return render(request, 'forms/login.html', {'form': form})


