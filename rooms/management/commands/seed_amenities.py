from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):

    def handle(self, *args, **options):
        amenities = [     
            "Kitchen",
            "Shampoo",
            "Heating",
            "Air conditioning",
            "Washing machine",
            "Dryer",
            "Wifi",
            "Breakfast",
            "Indoor fireplace",
            "Hangers",
            "Iron",
            "Hair dryer",
            "Dedicated workspace",
            "TV",
            "Cot",
            "High chair",
            "Self check-in",
            "Smoke alarm",
            "Carbon monoxide alarm",
            "Private bathroom",
            "Piano",
        ]
        for a in amenities:
            room_models.Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))