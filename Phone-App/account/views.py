from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from . forms import NewUserRegister
from django.contrib import messages
# Create your views here.
def createuser(request):
    myform=NewUserRegister()
    if request.method=='POST':
        myform=NewUserRegister(request.POST)
        if myform.is_valid():
            myform.save()
            messages.info(request,'Registred successfully you can login now.')
            return redirect('login')
    return render(request,'account/createuser.html',{'myform':myform,})


# Create login function 
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Invalid username or password')
    return render(request,'account/login.html')


# Create function logout
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request,'account/logout-user.html')