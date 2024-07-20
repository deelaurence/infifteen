from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, View
from .forms import *
from .models import Profile
from django.shortcuts import render, redirect
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
import logging
import requests

from decouple import config


brevo_key = config('BREVO_KEY')


logger = logging.getLogger(__name__)

class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('mail-sent')
    
    def form_valid(self, form):
        print('trying to signup')
        user = form.save()
        print(form.cleaned_data['name'])
        Profile.objects.get_or_create(user=user, defaults={'name': form.cleaned_data['name']})
        
        # Send verification email
        self.send_verification_email(user, form.cleaned_data['email'])
        
        return super().form_valid(form)
    
    def form_invalid(self, form):    
        print('Signup form is not valid')    
        return super().form_invalid(form)

    def send_verification_email(self, user, email):
        try:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            verification_link = self.request.build_absolute_uri(reverse_lazy('verify_email', kwargs={'uidb64': uid, 'token': token}))

            subject = 'Verify your email address'
            message = render_to_string('users/verification_email.html', {
                'user': user,
                'verification_link': verification_link,
            })

            logger.debug(f'Sending email to {email}')

            api_url = "https://api.sendinblue.com/v3/smtp/email"
            payload = {
                "sender": {"name": "InFifteen", "email": "deverence@infifteen.com"},
                "to": [{"email": email}],
                "subject": subject,
                "htmlContent": message
            }
            headers = {
                "accept": "application/json",
                "api-key": brevo_key,
                "content-type": "application/json"
            }

            response = requests.post(api_url, json=payload, headers=headers)

            if response.status_code == 201:
                logger.debug('Email sent successfully')
            else:
                logger.error(f'Error sending email: {response.text}')
        except Exception as e:
            logger.error(f'Error sending email: {e}')


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('dashboard') 

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        if not User.objects.filter(email=email).exists():
            form.add_error(None, 'Email not registered')
            return self.form_invalid(form)
        user = authenticate(username=email, password=password)
        profile = Profile.objects.get(user=user)
        print('verified is',profile.is_verified)
        if not profile.is_verified:
            form.add_error(None, 'Email not verified')
            return self.form_invalid(form)
        print(user)
        if user is not None:
            login(self.request, user)
        else:
            form.add_error(None, 'Invalid Credentials')
            return self.form_invalid(form)    
        return super().form_valid(form)

    def form_invalid(self, form):    
        print('Login form is not valid')    
        print(form.errors.items())
        return self.render_to_response(self.get_context_data(form=form))
        return super().form_invalid(form)


class VerifyEmailView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            profile = Profile.objects.get(user=user)
            print(profile)
            profile.is_verified = True
            profile.save()
            return redirect('login')
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
            return render(request, 'users/verification_failed.html')
        



class CheckYourMail(View):
    def get(self, request):
        
        return render(request, 'users/mail_sent.html')
        
