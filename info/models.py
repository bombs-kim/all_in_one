from django.db import models
from master.models import Master

# class NeworderInfo(models.Model):
#     SITE_CHOICES = (
#         ('GMKT', 'G Market'),
#         ('Auction', 'Auction'),
#     )
#
#     master = models.ForeignKey(Master, related_name='neworders')
#
#     site = models.CharField(max_length=100, choices=SITE_CHOICES)
#
#     cp = models.CharField(max_length=100)
#     ht = models.CharField(max_length=100)
#     id = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#
#     goodsName = models.CharField(max_length=100)
#     goodsNo = models.CharField(max_length=100)
#     price = models.CharField(max_length=100)
#     cartNo = models.CharField(max_length=100)
#     depositConfirmDate = models.CharField(max_length=100)
#
#     deliveryFeetype = models.CharField(max_length=100)
#     rcverAddr = models.CharField(max_length=100)
#     rcverCp = models.CharField(max_length=100)
#     rcverHt = models.CharField(max_length=100)
#
#     sellerID = models.CharField(max_length=100)
#
#     def __str__(self):
#         return "for {}".format(self.master.user.username)
