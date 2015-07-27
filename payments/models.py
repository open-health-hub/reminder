from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):
    owner = models.OneToOneField(User)
    stripe_subscription_id = models.CharField(blank=True, max_length=100)
