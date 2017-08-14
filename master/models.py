from django.db import models
from django.conf import settings

class Master(models.Model):
    # Associated with django User model
    # (django.contrib.auth.User by default)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

class Account(models.Model):
    master = models.ForeignKey(
        to=Master, related_name='accounts')
