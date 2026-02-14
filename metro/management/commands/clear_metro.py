from django.core.management.base import BaseCommand

from metro.models import Metro, MetroLine


class Command(BaseCommand):
    def handle(self, *args, **options):
        MetroLine.objects.all().delete()
        Metro.objects.all().delete()
