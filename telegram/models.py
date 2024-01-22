#from django.contrib.auth.models import User
from django.db import models
from requests import request
from datetime import datetime, timedelta
# Create your models here.

class Plan(models.TextChoices):
    Month = 'Month'

class TelegramGroup(models.Model):
    planType = models.CharField(max_length=50, choices=Plan.choices)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return str(self.planType)
    
class SubActive(models.Model):
    if TelegramGroup.objects.filter(planType = 'Month'):
        isPlan = 'Month'
        #if request.method == 'POST':
        dys=30
    elif TelegramGroup.objects.filter(planType = '3 Months'):
        isPlan = '3 Months'
        #if request.method == 'POST':
        dys=90
    elif TelegramGroup.objects.filter(planType = '6 Months'):
        isPlan = '6 Months'
        #if request.method == 'POST':
        dys=180
    elif TelegramGroup.objects.filter(planType = 'one year') :
        isPlan = 'one year'
        #if request.method == 'POST':
        dys=365
    else:
        isPlan = 'none'
              
    #is_planType = models.ForeignKey(TelegramGroup('planType'), blank=True, null=True, on_delete=models.SET_NULL)
    is_planType = models.CharField(max_length=30, null=False, default=isPlan)
    payID = models.CharField(max_length=255, blank=True, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    startTime = models.DateTimeField(default=datetime.now())
    endTime = models.DateTimeField(default=datetime.now())
    is_active = models.BooleanField(default=False)
    nameTelegram = models.CharField(max_length=75)
    #def __str__(self):
     #   return str(self.nameTelegram)