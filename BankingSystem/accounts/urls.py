from django.conf.urls import url
from django.urls import path
from django.contrib.auth import update_session_auth_hash

from . import views

from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    url(r"^register/$", views.register, name="signup"),
    url(r"^login/$", views.sign_in, name="signin"),
    url(r"^logout/$", views.logout_view, name="logout"),
# Forget password

    url(r'^reset_password/$', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html'), name='reset_password'),
    url(r'^reset_password_sent/$', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^reset_password_complete/$', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),

]
