from django.shortcuts import render, redirect
from . import forms
from . import models
from . forms import DepositForm, Loan, WithdrawForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from profiles.models import Status,Deposit,Loan,Withdraw

import random


def randomGen():
    # return a 6 digit random number
    return int(random.uniform(100000, 999999))


def index(request):
    try:
        curr_user = Status.objects.get(user_name=request.user)  # getting details of current user
    except:
        # if no details exist (new user), create new details
        curr_user = Status()
        curr_user.account_number = randomGen()  # random account number for every new user
        curr_user.balance = 0
        curr_user.user_name = request.user
        curr_user.save()
    return render(request, "profiles/profile.html", {"curr_user": curr_user})


def money_transfer(request):
    if request.method == "POST":
        form = forms.MoneyTransferForm(request.POST)
        if form.is_valid():
            form.save()

            curr_user = models.MoneyTransfer.objects.get(enter_your_user_name=request.user)
            dest_user_acc_num = curr_user.enter_the_destination_account_number

            temp = curr_user  # NOTE: Delete this instance once money transfer is done

            dest_user = models.Status.objects.get(account_number=dest_user_acc_num)  # FIELD 1
            transfer_amount = curr_user.enter_the_amount_to_be_transferred_in_Npr  # FIELD 2
            curr_user = models.Status.objects.get(user_name=request.user)  # FIELD 3

            # Now transfer the money!
            curr_user.balance = curr_user.balance - transfer_amount
            dest_user.balance = dest_user.balance + transfer_amount

            # Save the changes before redirecting
            curr_user.save()
            dest_user.save()

            temp.delete()  # NOTE: Now deleting the instance for future money transactions

        return redirect("profiles/profile.html")
    else:
        form = forms.MoneyTransferForm()
    return render(request, "profiles/money_transfer.html", {"form": form})


def loan(request):
    form=Loan()
    if request.method == "POST":
        form = forms.Loan(request.POST)
        if form.is_valid():
            form.save()
            

            curr_user = models.Loan.objects.get(enter_your_user_name=request.user)
            dest_user_acc_num = curr_user.enter_the_your_account_number

            temp = curr_user  # NOTE: Delete this instance once money transfer is done

            dest_user = models.Status.objects.get(account_number=dest_user_acc_num)  # FIELD 1
            transfer_amount = curr_user.enter_the_amount_to_be_transferred_in_Npr  # FIELD 2
            curr_user = models.Status.objects.get(user_name=request.user)  # FIELD 3
            

            # Now transfer the money!
            curr_user.balance = curr_user.balance + transfer_amount
            dest_user.balance = dest_user.balance + transfer_amount
            

            # Save the changes before redirecting
            curr_user.save()
            dest_user.save()

            temp.delete()  # NOTE: Now deleting the instance for future money transactions

        return redirect("profiles/profile.html")
    else:
        form1 = forms.Loan()
        return render(request, "profiles/loan_app.html", {"form1": form1})



def withdraw_money(request):
    form=WithdrawForm()
    if request.method=="POST":
        form=forms.WithdrawForm(request.POST)
        if form.is_valid():
            form.save()
            curr_user1 = request.user
            

            # temp = curr_user1  # NOTE: Delete this instance once money transfer is done
            acc=models.Status.objects.get(user_name=curr_user1.username)
            acc_num=models.Status.objects.get(id=acc.id)
            
            # curr_user = models.Status.objects.get(user_name=request.username) 
            

        
            withdraw_amount = request.POST['amount']

        
            acc_num.balance = acc_num.balance - int(withdraw_amount)
        
        
            

            withdraw= models.Deposit.objects.create(username=curr_user1.username,
            account_number=acc_num.account_number,amount=withdraw_amount)
            if withdraw:
                acc_num.save()

            # temp.delete()  # NOTE: N
            messages.success(request,'Money withdrawn sucessfully')
            return redirect('profiles/profile.html')
        else:
            messages.error(request,'Unable to withdraw amount')
            return render(request, "profiles/withdraw_money.html",{'form':form})
    context={
        'form': form,
        
    }
   
    return render(request, "profiles/withdraw_money.html",context)
    



def deposit(request):
    form=DepositForm()
    if request.method=="POST":
        form=forms.DepositForm(request.POST)
        if form.is_valid():
            form.save()
            curr_user1 = request.user
            

            # temp = curr_user1  # NOTE: Delete this instance once money transfer is done
            acc=models.Status.objects.get(user_name=curr_user1.username)
            acc_num=models.Status.objects.get(id=acc.id)
            
            # curr_user = models.Status.objects.get(user_name=request.username) 
            

        
            deposit_amount = request.POST['amount']

        
            acc_num.balance = acc_num.balance + int(deposit_amount)
        
        
            

            deposit= models.Deposit.objects.create(username=curr_user1.username,
            account_number=acc_num.account_number,amount=deposit_amount)
            if deposit:
                acc_num.save()

            # temp.delete()  # NOTE: N
            messages.success(request,'Money deposited sucessfully')
            return redirect('profiles/profile.html')
        else:
            messages.error(request,'Unable to add deposit')
            return render(request, "profiles/deposit_money.html",{'form':form})
    context={
        'form': form,
        
    }
    return render(request, "profiles/deposit_money.html",context)
    


def settings(request):
    return render(request, "profiles/settings.html")


def edit_details(request):
    if request.method == "POST":
        # POST actions for BasicDetailsForms
        try:
            curr_user = models.BasicDetails.objects.get(user_name=request.user)
            form = forms.BasicDetailsForm(request.POST, instance=curr_user)
            if form.is_valid():
                form.save()
        except:
            form = forms.BasicDetailsForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user_name = request.user
                form.save()

        # POST actions for PresentLocationForm
        try:
            curr_user = models.PresentLocation.objects.get(user_name=request.user)
            form = forms.PresentLocationForm(request.POST, instance=curr_user)
            if form.is_valid():
                form.save()
        except:
            form = forms.PresentLocationForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user_name = request.user
                form.save()

                # POST actions for Password change
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')

        return redirect("profiles/edit_details.html")

    else:  # GET actions
        try:
            curr_user = models.BasicDetails.objects.get(user_name=request.user)
            form1 = forms.BasicDetailsForm(instance=curr_user)  # basic details
        except:
            form1 = forms.BasicDetailsForm()

        try:
            curr_user = models.PresentLocation.objects.get(user_name=request.user)
            form2 = forms.PresentLocationForm(instance=curr_user)  # location
        except:
            form2 = forms.PresentLocationForm()

        # change password
        form3 = PasswordChangeForm(request.user)

        dici = {"form1": form1, "form2": form2, "form3": form3}
        return render(request, "profiles/edit_details.html", dici)


def delete_account(request):
    return render(request, "profiles/delete_account.html")# Create your views here.
