from django.core.management.base import BaseCommand
from core.models import *

class Command(BaseCommand):
    help = 'Insert some test data into the database'

    def handle(self, *args, **kwargs):
        