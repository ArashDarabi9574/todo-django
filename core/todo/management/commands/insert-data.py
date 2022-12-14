from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import Profile
from todo.models import Task
import random
from datetime import datetime
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "inserting random task into database"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.fake.email(), password="test@1234")
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.description = self.fake.paragraph(nb_sentences=5)
        profile.save()

        for _ in range(5):
            Task.objects.create(
                user=user,
                title=self.fake.paragraph(nb_sentences=1),
                complete=random.choice([True, False]),
                created_date=datetime.now(),
            )
