from django.conf.urls import url
from . import views
from django.urls import path

app_name = "admins"

urlpatterns = [
    url(r"^$", views.admin_dashboard, name = "admin_dashboard"),
    url(r'^profiles/',views.user_account,name="profiles"),
    url(r'^show-user/',views.get_user,name="show-user"),
    url(r'^admin_dashboard/',views.admin_dashboard,name="admin_dashboard"),
    path('update_user_to_admin/<int:user_id>',views.update_user_to_admin,name="updateadmin"),
    path('demote_admin_to_user/<int:user_id>',views.demote_admin_to_user,name="demoteadmin"),
    path('delete_user/<int:user_id>',views.delete_user,name="delete_user"),
    # path('search',views.search,name="search"),
    
]
