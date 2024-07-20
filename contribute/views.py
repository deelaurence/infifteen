from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView,UpdateView, FormView
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ContributeView(LoginRequiredMixin,CreateView):
    form_class = QuestionForm
    template_name = 'contribute/index.html'
    success_url = reverse_lazy('thanks')
    

    def form_valid(self, form):
        print('trying to contribute')
        form.instance.user = self.request.user
        form.save()
        # login(self.request, user)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors)    
        print('Contribute form is not valid')    
        return super().form_invalid(form)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories=Category.objects.all()
        context['categories'] = categories
        return context



# Create your views here.
class ThanksView(View):
    def get(self,request):
        return render(request,'contribute/thanks.html',{})
    

class EditQuestionView(LoginRequiredMixin,UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'contribute/edit_question.html'
    success_url = reverse_lazy('thanks')

    def form_valid(self, form):
        print('Editing question')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors)
        print('Edit form is not valid')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = self.object
        question=Question.objects.get(id=self.kwargs['pk'])
        categories=Category.objects.all()
        context['category'] = question.category
        
        # print(self.object.__dict__)
        return context