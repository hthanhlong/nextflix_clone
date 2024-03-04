from django.urls import path
from .views import login, signup, verify_otp, resend_otp, get_roles

urlpatterns = [
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('verify-otp', verify_otp, name='verify-otp'),
    path('resend-otp', resend_otp, name='resend-otp'),
    # get roles
    path('roles', get_roles, name='get-roles') 
]
