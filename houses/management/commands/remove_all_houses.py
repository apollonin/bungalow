from django.core.management.base import BaseCommand
from django.utils import timezone

from houses.models import House

class Command(BaseCommand):
    help = 'Remove all houses'

    def handle(self, *args, **kwargs):
        House.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Done"))