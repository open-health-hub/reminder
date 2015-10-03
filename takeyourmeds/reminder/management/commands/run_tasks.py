from django.core.management.base import BaseCommand

from ..models import ReminderTime

class Command(BaseCommand):
    def handle(self, **options):
        for reminder_time in ReminderTime.objects.all():
            if reminder_time.should_run():
                reminder_time.run()
