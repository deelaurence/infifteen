from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.template.loader import render_to_string
import requests
from django.urls import reverse_lazy
from decouple import config

brevo_key = config('BREVO_KEY')


class Question(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    question_text = models.TextField()
    optionA = models.CharField(max_length=255)
    optionB = models.CharField(max_length=255)
    optionC = models.CharField(max_length=255, null=True, blank=True)
    optionD = models.CharField(max_length=255, null=True, blank=True)
    answer = models.CharField(max_length=255)
    category = models.CharField(max_length=255, null=True, blank=True)
    publish = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.pk:
            previous = Question.objects.get(pk=self.pk)
            if not previous.publish and self.publish:
                self.send_publish_email()
        if self.category:
            self.category = self.category.lower().strip()
        super(Question, self).save(*args, **kwargs)

    def send_publish_email(self):
        if self.user and self.user.email:
            try:
                subject = 'Your Question has been Published'
                
                message = render_to_string('contribute/question_published.html', {
                    'user': self.user,
                    'question': self
                })
                api_url = "https://api.sendinblue.com/v3/smtp/email"
                payload = {
                    "sender": {"name": "InFifteen", "email": "deverence@infifteen.com"},
                    "to": [{"email": self.user.email}],
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
                    print('Email sent successfully')
                else:
                    print(f'Error sending email: {response.text}')
            except Exception as e:
                print(f'Error sending email: {e}')

    def __str__(self):
        return self.question_text


class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category
