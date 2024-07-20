from django.urls import path
from .views import *


urlpatterns=[
    path("contribute/",ContributeView.as_view(),name='contribute' ),
    path("thanks/",ThanksView.as_view(),name='thanks' ),
    path('contribute/edit/<int:pk>/', EditQuestionView.as_view(), name='edit_question'),
]