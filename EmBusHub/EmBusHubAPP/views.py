from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def SignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass']
        c_password = request.POST['c_pass']
        
        if password == c_password:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email Unavailable')
                return redirect('register')
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username Unavailable')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('home')
        else:
            messages.info(request, "Passwords don't match")
            return redirect('register')
        
    return render(request, 'signup.html')
    
def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user.DoesNotExist:
            messages.error(request, "Doesn't Exist")
            return redirect('register')
        else:
            auth.login(request, user)
            messages.error(request, "Logged In")
            return redirect('home')
        
    return render(request, 'login.html')

def Logout(request):
    auth.logout(request)
    return redirect('home')

def Home(request):
    return render(request, 'index.html')

def Product(request):
    return render(request, 'products.html')
    
def ProductDetail(request):
    return render(request, 'product-detail.html')