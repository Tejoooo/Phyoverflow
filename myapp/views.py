from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.filter(email = email)
        except:
            messages.error(request,"User doesnt exist!")
            return redirect('login')
        user = authenticate(request,email=email,password=password)
        if user is not None:
            return redirect('index')
        else:
            messages.error(request,"User Credentials doesnot matched")
            return redirect('login')
    return render(request,'login.html')