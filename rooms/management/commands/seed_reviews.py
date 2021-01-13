import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from reviews import models as reivew_models
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        all_users = user_models.User.objects.all()
        all_rooms = room_models.Room.objects.all()

        seeder.add_entity(reivew_models.Review, number, {
           "review":lambda x: seeder.faker.sentence(),
           "accuracy":lambda x: random.randint(0, 5),
           "communication":lambda x: random.randint(0, 5),
           "cleanliness":lambda x: random.randint(0, 5),
           "lacation":lambda x: random.randint(0, 5),
           "check_in":lambda x: random.randint(0, 5),
           "value":lambda x: random.randint(0, 5),
           "user":lambda x: random.choice(all_users),
           "room":lambda x: random.choice(all_rooms),
        })        
        seeder.execute()        
        self.stdout.write(self.style.SUCCESS(f"{number} reviews created"))