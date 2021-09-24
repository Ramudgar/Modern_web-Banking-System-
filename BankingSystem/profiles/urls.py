from django.conf.urls import url
from . import views

app_name = "profiles"

urlpatterns = [
    url(r"^account_status/$", views.index, name="account_status"),
    url(r"^money_transfer/", views.money_transfer, name="money_transfer"),
    url(r"^loan_app/", views.loan, name="loan_app"),
    url(r"^withdraw/", views.withdraw_money, name="withdraw"),
    url(r"^deposit/", views.deposit, name="deposit"),
    url(r"settings/", views.settings, name="settings"),
    url(r"edit_details/", views.edit_details, name="edit_details"),

    url(r"delete_account/", views.delete_account, name="delete_account"),
    
]
