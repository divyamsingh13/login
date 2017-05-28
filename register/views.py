

from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .forms import UserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


def mainpage(request):
    return render(request,"mainpage.html")


def register(request):

    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            print("hello")
            username=form.cleaned_data['username']
            password=form.cleaned_data['password2']
            user=User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password2'],email=form.cleaned_data['email'])
            print("hello again")
            user = authenticate(username=username, password=password)
            if user is not None:
                print("hello None")
                if user.is_active:
                    print("hello login")
                    login(request, user)
                    return redirect('/')
    form=UserForm()
    context={'form':form}
    print("hello")

    return render(request,'register.html',context)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')



def login_page(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            print("hello")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if request.user.is_authenticated():
                login(user,request)
                return redirect('/')






