from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
import random


class GetAuthorQuestions(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        print(request.user)
        questions = list(Question.objects.filter(user=request.user))
        context = {
            'questions': questions,
        }

        return render(request, 'dashboard/index.html', context)

