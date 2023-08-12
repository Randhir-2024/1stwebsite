from django.shortcuts import render
from .models import *

def home(request):
    
    return render(request,'index.html')

def login(request):
    
    return render(request,'login.html')

def signup(request):
    
    return render(request,'signup.html')

def Register(request):
    if request.method == 'POST':
        Name=request.POST.get('Name')
        Phone=request.POST.get('Phone')
        Address=request.POST.get('Address')
        Password=request.POST.get('Password')
        
       
        try:
            if  User.objects.get(phone=Phone):
                return render(request,'login.html',{'msg':'User already exists'})
        except: 
            newuser=User.objects.create(name=Name,phone=Phone,address=Address,password=Password)
            
            return render(request,'login.html',{'msg':'Registration successful'})
    
