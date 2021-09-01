from django.urls import path, include

urlpatterns=[
    path('system/',include('system.urls')),
    path('admins',include('admins.urls')),
    path('',include('account.urls')),
]