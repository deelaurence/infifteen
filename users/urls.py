from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name='login' ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('mail-sent/',CheckYourMail.as_view() ,name="mail-sent"),
    path('verify-email/<uidb64>/<token>/', VerifyEmailView.as_view(), name='verify_email'),
    
]