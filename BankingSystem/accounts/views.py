from accounts.auth import unauthenticated_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm
from profiles.models import BasicDetails

@unauthenticated_user
def sign_in(request):
    if request.user.is_authenticated:
        return redirect('profiles:account_status')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                if auth.is_staff:
                    login(request, auth)
                    return redirect('admins:admin_dashboard')
                elif not auth.is_staff:
                    login(request, auth)
                    return redirect('profiles:account_status')
            else:
                messages.error(request, 'username and password doesn\'t match')
    return render(request, "accounts/sign_in.html")




@unauthenticated_user
def register(request):
    form = RegistrationForm(request.POST or None)

    if form.is_valid():
        user=form.save()
        BasicDetails.objects.create(user=user,user_name=user.username)
        messages.success(request, 'user registered successfully')
        return redirect('accounts:signin')
    return render(request, 'accounts/register.html', {'form':form})

@login_required
def logout_view(request):
    # Logout the user if he hits the logout submit button
    logout(request)
    return redirect("accounts:signin")

