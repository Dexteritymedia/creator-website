import random
from decimal import Decimal

from django.conf import settings
from django.core.management.base import BaseCommand

from faker import Faker

from app.models import Activity, Category


class Command(BaseCommand):
    help = 'Populate the Activity model with 100,000 entries'

    def handle(self, *args, **kwargs):
        fake = Faker()

        cities = [
            {'LGA': 'Ibadan North ', 'latitude': 3.91, 'longitude': 7.41},
            {'LGA': 'Ibadan North-East', 'latitude': 3.93, 'longitude': 7.36},
            {'LGA': 'Ibadan North-West', 'latitude':  3.87, 'longitude': 7.38},
            {'LGA': 'Ibadan South-East', 'latitude': 3.9114, 'longitude': 7.3293},
            {'LGA': 'Ibadan South-West', 'latitude': 3.8757, 'longitude': 7.3458},
            {'LGA': 'Akinyele', 'latitude': 3.9177, 'longitude': 7.5952},
            {'LGA': 'Egbeda', 'latitude': 3.9675, 'longitude': 7.3796},
            {'LGA': 'Ido', 'latitude': 3.7194, 'longitude': 7.5077},
            {'LGA': 'Lagelu', 'latitude': 4.0491, 'longitude': 7.4846},
            {'LGA': 'Ona Ara', 'latitude': 4.0491, 'longitude': 7.2689},
            {'LGA': 'Oluyole', 'latitude': 3.8655, 'longitude': 7.2059},
        ]

        categories = ['Stay', 'Food And Drink', 'Leisure']
        num_entries = 100000
        batch_size = 5000
        entries = []

        self.stdout.write(self.style.NOTICE('Populating the database...'))

        #for _ in range(num_entries):
        for i in range(num_entries):
            name = fake.company()
            city_lga = random.choice(cities) #random.choices(cities) returns a list
            address = fake.address()
            price = Decimal(f"{random.uniform(500.00, 100000.00):.2f}")
            categories = random.choice(['Stay', 'Food And Drink', 'Leisure'])#Use the list directly instead of variable "categories" because of the forloop

            entries.append(Activity(
                category=Category.objects.get_or_create(
                    name=categories,
                )[0],
                name=name,
                location=f"{address}, {city_lga['LGA']}",
                cost=price,
                latitude=city_lga['latitude'],
                longitude=city_lga['longitude']
            ))

            if (i + 1) % batch_size == 0:
                Activity.objects.bulk_create(entries)
                entries.clear()

                remaining_entries = num_entries - (i + 1)
                self.stdout.write(self.style.SUCCESS(f'Successfully populated {i + 1} activities. Remaining {remaining_entries}'))
            """  
            #Batch save every 5000 records to avoid memory issues
            if len(entries) == 5000:
                Activity.objects.bulk_create(entries)
                self.stdout.write(self.style.SUCCESS(f'Successfully populated 5000 activities'))
                entries.clear()
            """

        if entries:
            Activity.objects.bulk_create(entries) #Save any remaining entries

        all_entries = Activity.objects.count()
        self.stdout.write(self.style.SUCCESS(f'Successfully populated 100,000 activities. All entries {all_entries}'))
