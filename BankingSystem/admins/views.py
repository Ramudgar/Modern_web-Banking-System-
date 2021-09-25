from admins.filters import LoanFilter
from profiles.views import loan, withdraw_money
from django.contrib.auth.decorators import login_required
from accounts.auth import admin_only
from profiles import models
from profiles import forms

from django.contrib.auth.models import User

from django.shortcuts import render,redirect
from django.contrib import messages

from django.core.paginator import Paginator
from django.db.models import Q

@login_required
@admin_only
def index(request):
    return render(request, "admins/dashboard.html")

@login_required
@admin_only
def user_account(request):
    if request.method == "POST":
            # POST actions for BasicDetailsForms
        try:
            curr_user = models.BasicDetails.objects.get(user_name=request.user)
            form = forms.BasicDetailsForm(request.POST, request.FILES,instance=curr_user)
            if form.is_valid():
                form.save()
                
        except:
            form = forms.BasicDetailsForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user_name = request.user
                form.save()  
        return redirect("admins:profiles")        
            
    else:
        try:
            curr_user = models.BasicDetails.objects.get(user_name=request.user)
            form1 = forms.BasicDetailsForm(instance=curr_user) # basic details
        except:
            form1 = forms.BasicDetailsForm()

        context = {
            "form1": form1,
            'activate_profiles':'active'
            }
        return render(request, "admins/profiles.html", context)

@login_required
@admin_only
def admin_dashboard(request):
    users=User.objects.filter(is_staff=0)
    user_count=users.count()
    admins=User.objects.filter(is_staff=1)
    admin_count=admins.count()
    loan=models.Loan.objects.all()
    loan_count=loan.count()
    money=models.MoneyTransfer.objects.all()
    money_count=money.count()
    deposit=models.Deposit.objects.all()
    deposit_count=deposit.count()
    withdraw=models.Withdraw.objects.all()
    withdraw_count=withdraw.count()
    context={
        'users':user_count,
        'admins':admin_count,
        'loan_count':loan_count,
        'money_count':money_count,
        'deposit_count':deposit_count,
        'withdraw_count':withdraw_count
    }
    return render(request, 'admins/dashboard.html',context)

@login_required
@admin_only
def get_user(request):
    loan=models.Loan.objects.all()
    paginator = Paginator(loan, 5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    users_all=User.objects.all()
    users=users_all.filter(is_staff=0)
    users_admin=users_all.filter(is_staff=1)
    deposit=models.Deposit.objects.all()
    withdraw=models.Withdraw.objects.all()
    transfer=models.MoneyTransfer.objects.all()
    
    
	
    context={
        'users':users,
        'users_admin':users_admin,
        'activate_showuser':'active',
        'loan':page_obj,
        'deposit':deposit,
        'withdraw':withdraw,
        'transfer':transfer,
    }
    return render (request,'admins/showuser.html',context)


# def search(request):
#     loans = models.Loan.objects.all().order_by('-id')
#     loan_filter = LoanFilter(request.GET, queryset=loans)
#     loan_final = loan_filter.qs
#     context = {
#         'loans': loan_final,
#         'activate_student': 'active',
#         'loan_filter': loan_filter
#     }
#     return render(request, 'admins/showuser.html', context)





@login_required
@admin_only
def update_user_to_admin(request,user_id):
    user=User.objects.get(id=user_id)
    user.is_staff=True
    user.save()
    messages.success(request,'User has been updated to Manager')
    return redirect('admins:show-user')

@login_required
@admin_only
def demote_admin_to_user(request,user_id):
    user=User.objects.get(id=user_id)
    user.is_staff=False
    user.save()
    messages.success(request,'Admin has been demoted to user')
    return redirect('admins:show-user')

@login_required
@admin_only
def delete_user(request,user_id):

    user=User.objects.get(id=user_id)
    user.delete()
    messages.success(request, 'Your account has been deleted successfully.')
    return redirect('admins:show-user')
    

  