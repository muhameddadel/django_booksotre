from django.contrib.auth import views
from django.urls import path

from .forms import *
from .views import *

app_name = 'account'

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='account/registration/login.html', form_class=UserLoginForm), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
    path('register/', account_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>', account_activate, name='activate'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/edit/', edit_details, name='edit_details'),
]
