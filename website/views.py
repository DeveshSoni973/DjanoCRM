from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    #check for logging in
    records=Record.objects.all()
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
        return render(request, 'home.html', {'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, "YOU HAVE BEEN LOGGED OUT...")
    return redirect('home')

'''In the register_user function, the {} is used to pass context data to the template. The render function in Django takes at least three arguments:

The request object, which represents the HTTP request.
The path to the template file as a string.
A dictionary ({} in your example) that contains context data to be used in the template
'''
def register_user(request):
    if request.method == 'POST':  # Corrected 'POST' to uppercase
        form = SignUpForm(request.POST)  # Bind form with POST data
        if form.is_valid():
            user = form.save()  # Save the user to the database
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'You have been successfully registered and logged in.')
            return redirect('home')
        else:
            messages.error(request, 'There was an error during registration. Please try again.')
    else:
        form = SignUpForm()  # Create an empty form instance for GET request
        return render(request, 'register.html', {'form': form}) 
    return render(request, 'register.html', {'form': form}) 

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record=Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, 'You must be logged in for this!!!')
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it=Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Deletion Successful')
        return redirect('home')
    else:
        messages.success(request, 'You must be logged in for this!!!')
        return redirect('home')

def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(request, "Record Added...")
                return redirect('home')    
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "YOU MUST BE LOGGED IN...")
        return redirect('home')   


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')