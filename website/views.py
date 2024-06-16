from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def home(request):
    #check for logging in
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "YOU HAVE BEEN LOGGED IN...")
            return redirect('home')
        else:
            messages.success(request, "There was an error. TRY AGAIN")
            return redirect('home')

    else:
        return render(request, 'home.html', {})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "YOU HAVE BEEN LOGGED OUT...")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})


'''In the register_user function, the {} is used to pass context data to the template. The render function in Django takes at least three arguments:

The request object, which represents the HTTP request.
The path to the template file as a string.
A dictionary ({} in your example) that contains context data to be used in the template
'''


