from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from Auth_app.EmailBackEnd import EmailBackEnd
from django.contrib import messages
from Auth_app.models import CustomUser
from django.urls import reverse

# Create your views here.


def Registration(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        
        
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exist!')
            return redirect('Auth_app:rejistration')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exist!')
            return redirect('Auth_app:rejistration')
        
        user = CustomUser(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email,
            gender = gender,
            profile_pic = profile_pic
        )
        user.set_password(password)
        user.save()
        return redirect('Auth_app:login')
    return render(request, 'Auth_app/Registration.html')

def Login_form(request):
    context = {
       
    }
    return render(request, 'Auth_app/Login.html', context)

def Do_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = EmailBackEnd.authenticate(request, username=email, password=password)
        
        if user!=None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email and Password are not same!')
            return redirect('Auth_app:login')
    else:
        messages.error(request, 'Email and Password are not same!')
        return redirect('Auth_app:login')
    
    
def Do_logout(request):
    logout(request)
    return redirect('home')


def Profile(request):
    return render(request, 'Auth_app/profile.html')


def Edit_profle(request, id):
    user = CustomUser.objects.get(id=id)
    context={
        'user':user
    }
    return render(request, 'Auth_app/edit_pro.html', context)

def Update_profile(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # username = request.POST.get('username')
        # email = request.POST.get('email')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            
            if password !=None and password !='':
                customuser.set_password(password)
            if profile_pic !=None and profile_pic !='':
                customuser.profile_pic=profile_pic
                
            if gender !=None and gender !='':
                customuser.gender = gender
                
            customuser.save()
            messages.success(request, 'Profile Successfully Updated!')
            return redirect('Auth_app:profile')
        except:
            messages.error(request, 'Profile Not Updated!')
            return redirect('Auth_app:edit_profile')
    return render(request, 'Auth_app/edit_pro.html', context={})
        
        
   