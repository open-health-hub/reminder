from django.contrib import admin

from .models import Subscription
# Register your models here.

@admin.register(Subscription)
class Subscription(admin.ModelAdmin):
    list_display = [
        'id',
        'stripe_subscription_id',
    ]
