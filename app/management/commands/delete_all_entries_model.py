import random

from django.conf import settings
from django.core.management.base import BaseCommand

from faker import Faker

from app.models import Activity


class Command(BaseCommand):
    help = 'Populate the House model with 100,000 entries'

    def handle(self, *args, **kwargs):
        

        self.stdout.write(self.style.NOTICE('Deleting the database...'))

        all_entries = Activity.objects.count()
        
        entries = Activity.objects.all()
        entries.delete()

        
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {all_entries}'))
