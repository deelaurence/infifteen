import string
import random
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    top_languages = models.JSONField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

def generate_random_username(name, length=8):
    """Generates a random username starting with the user's name."""
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return f"{name}_{random_string}"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    print('Post save signal sent from users new user=', created)
    if created:
        print('Inner post save signal sent from users new users=', created)
        # Use the first part of the user's email before "@" as the name for username generation
        name_part = instance.email.split('@')[0]
        instance.username = generate_random_username(name_part)
        print(instance)
        instance.save(update_fields=['username'])
    Profile.objects.get_or_create(user=instance)
        