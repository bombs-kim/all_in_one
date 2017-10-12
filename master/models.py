from django.db import models
from django.conf import settings

class Master(models.Model):
    """
    Associated with django User model.
    django User model is django.contrib.auth.models.User type by default
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    nickname = models.CharField(max_length=100, default='')

    def __str__(self):
        return '{}({})'.format(self.user, self.nickname)

class Account(models.Model):
    SITE_CHOICES = (
        ('ESM', 'ESM'),
        ('GMKT', 'G Market'),
        ('AUC', 'Auction'),
        ('STOREFARM', 'Naver Store farm'),
        ('STOREFARM_NID', 'Naver Store farm NID'),
        ('CAFE24', 'Cafe 24')
    )
    master = models.ForeignKey(Master, related_name='accounts')
    site = models.CharField(max_length=100, choices=SITE_CHOICES)
    userid = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    domain = models.CharField(max_length=150, blank=True)  # needed for cafe24

    def __str__(self):
        return '(ID: {})'.format(self.userid)
