from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

from django.urls import reverse
from django.views import View
from contribute.models import Question
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .randomizeOptions import randomly_switch_dict_items
import random
from django.middleware.csrf import get_token


class GetQuizInCategory(View):
    def get(self, request, category, *args, **kwargs):
        questions = list(Question.objects.filter(category=category, publish=True))
        random.shuffle(questions)
        
        # Randomize options for all questions
        for question in questions:
            if question.optionC is None:
                question.optionC = ''  # Or any default value you prefer
            if question.optionD is None:
                question.optionD = ''
            # print(question.__dict__)
            modified_dict = randomly_switch_dict_items(question.__dict__)
            question.__dict__.update(modified_dict)
        
        all_results=list(Results.objects.exclude(percentage_score='').values())
        for single_result in all_results:
                if single_result['percentage_score']:
                    percentage_score = float(single_result['percentage_score'])
                    questions_attempted = float(single_result['questions_attempted'])

                    # Calculate fair_result as a float
                    fair_result = percentage_score * questions_attempted / 100.0

                    # Update single_result with fair_result
                    single_result['fair_result'] = round(fair_result,2)
             
        sorted_results=sorted(all_results, key=lambda x: x['fair_result'], reverse=True)



        context = {
            'questions': questions,
            'category':category,
            'leaderboard':sorted_results
        }

        return render(request, 'quiz/index.html', context)


    def post(self, request, category, *args, **kwargs):
            # Handle POST request logic here
            data = request.POST
            print(data)
            print("Session Key:", request.session.session_key)
            print("CSRF Token:", get_token(request))
            
            category=data.get('category')
            score = data.get('score')
            attempted_questions=data.get('attempted_questions')
            name=data.get('name')
            # print(category,score,attempted_questions)

            result=Results(category=category,percentage_score=score,questions_attempted=attempted_questions,name=name)
            
            result.save()

       
            return HttpResponseRedirect(reverse('quiz-in-category', args=[category]))

