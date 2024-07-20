from django.urls import path
from .views import GetAuthorQuestions


urlpatterns=[
    path('dashboard/',GetAuthorQuestions.as_view(), name='dashboard')
]