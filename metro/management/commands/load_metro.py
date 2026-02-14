from django.core.management.base import BaseCommand

from metro.parser import provider


class Command(BaseCommand):
    def handle(self, *args, **options):
        provider.download_all()
        self.stdout.write("Done")
