from django.contrib import admin
from .models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('status',)  # Add other fields if needed

    def get_status_display(self, obj):
        return obj.get_status_display()
    get_status_display.short_description = 'Status'

admin.site.register(Subscription, SubscriptionAdmin)
