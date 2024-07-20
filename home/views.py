from django.shortcuts import render
from django.views.generic import TemplateView
from contribute.models import Question

# Create your views here.

class Home(TemplateView):
    template_name = 'home/home.html'


    def get_context_data(self, **kwargs):
        
        questions = Question.objects.filter(publish=True)
        categories=questions.values_list('category',flat=True).distinct()
        numbersInCategory=questions.values_list('category',flat=True)
        categories_count={}

        for category in numbersInCategory:
            if category in categories_count:
                categories_count[category] += 1
            else:
                categories_count[category] = 1
            
        
        context = super().get_context_data(**kwargs)
        context['categories'] = len(categories)
        context['category'] = categories_count
        return context 