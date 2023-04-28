from django.db import models
from django.contrib.auth.models import User


class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    order_id = models.CharField(max_length=100)
    subscription_id = models.CharField(max_length=100)
    payment_source = models.CharField(max_length=100)
