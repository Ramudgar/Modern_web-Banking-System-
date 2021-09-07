
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm

def sign_in(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(request,username=data['username'],password=data['password'])

            if user is not None:
                login(request,user)
                return redirect("profiles:account_status")
            else:
                messages.add_message(request, messages.ERROR, 'Invalid user credentials')
                return render(request,"accounts/sign_in.html",{"form_login":form})


    context={
        "form_login":LoginForm,
        "activate_login":"active"
    }
    return render(request,"accounts/sign_in.html",context)
# def sign_in(request):
#     if request.method == "POST":
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect("profiles:account_status")
#     else:
#         form = AuthenticationForm()
#         return render(request, "accounts/sign_in.html", {"form": form})
def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'User registered Successfully')
            return redirect("accounts:signin")
        else:
            messages.add_message(request,messages.ERROR,'Unable to register user')
            return render(request,"accounts/register.html",{"form_register":form})

    context={
        "form_register":UserCreationForm,
        'activate_register':'active'
    }
    return render(request,"accounts/register.html",context)
# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("accounts:signin")
#     else:
#         form = UserCreationForm()
#     return render(request, "accounts/register.html", {"form": form})



def logout_view(request):
    # Logout the user if he hits the logout submit button
    logout(request)
    return redirect("accounts:signin")
