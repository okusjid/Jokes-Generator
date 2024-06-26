from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    joke = models.TextField(default='')

    def __str__(self):
        return f"{self.user.username}'s Profile"
