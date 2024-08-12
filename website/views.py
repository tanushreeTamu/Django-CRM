from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    # print(records)  # Logs the QuerySet to the console
    # for record in records:
    #     print(record)

    #check to see if they are logging in 
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request,"you ahve been logged in")
            return redirect('home')
        else:
            messages.success(request,"There was an error logging in .. please try again")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})


# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "you have been loggedout !!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request,user)
            messages.success(request, "You have successfully regstered.Welcome!!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
        
    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        #look up record
        print(id)
        customer_record = Record.objects.get(id = pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to see the record")
        return redirect('home')
    
def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id = pk)
        delete_it.delete()
        messages.success(request, "Record deleted successfully..")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete the record")
        return redirect('home')

def add_record(request):
    form =AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "record added..")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in..")
        return redirect('home')
    
def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id = pk)
        form =AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid(): 
            form.save()
            messages.success(request, "Record has been updated")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in..")
        return redirect('home')

            