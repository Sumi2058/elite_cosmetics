from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from users.models import User,UserForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})  
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user_detail.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

def user_update(request, pk):
    user= get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form})

def user_delete(request, pk):
    user= get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        User.delete()
        return redirect('user_list')
    return render(request, 'user_confirm_delete.html', {'user': user})


def login_view(request):
    if request.method == "POST":
        email= request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.get(email=email)

        if user is not None:
            ##login(request, user)
            messages.success(request, f"Welcome back, {user.email}!")
            return redirect("home")  # change to your homepage URL name
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "login.html")

def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()### It save the data into database
            return redirect('login')
  
    return render(request, 'register.html')

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("login")

