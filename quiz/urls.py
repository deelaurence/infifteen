from django.urls import path
from .views import *


urlpatterns=[
    path('quiz/<str:category>/', GetQuizInCategory.as_view(), name='quiz-in-category'),
]