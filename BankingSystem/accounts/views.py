from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm


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
                    return redirect('admins:admin_index')
                elif not auth.is_staff:
                    login(request, auth)
                    return redirect('profiles:account_status')
            else:
                messages.error(request, 'username and password doesn\'t match')
    return render(request, "accounts/sign_in.html")





def register(request):
    form = RegistrationForm(request.POST or None)
    context={
        'form':RegistrationForm,
        'activate_signup':'active'
    }
    if form.is_valid():
        form.save()
        return redirect('accounts:signin')
    return render(request, 'accounts/register.html', context)

def logout_view(request):
    # Logout the user if he hits the logout submit button
    logout(request)
    return redirect("accounts:signin")

