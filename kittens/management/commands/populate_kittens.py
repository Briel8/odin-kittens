from django.core.management.base import BaseCommand
from kittens.models import Kitten

class Command(BaseCommand):
    help = 'Delete all existing kittens and populate the database with new kittens'

    def handle(self, *args, **kwargs):
        # Step 1: Delete all existing Kitten records
        self.stdout.write("Deleting all kittens...")
        Kitten.objects.all().delete()
        self.stdout.write("All kittens deleted successfully.")

        # Step 2: Predefine some kitten data
        kittens = [
            {'name': 'Fluffy', 'age': 1, 'cuteness': 'Very Cute', 'softness': 'Extremely Soft'},
            {'name': 'Mittens', 'age': 2, 'cuteness': 'Adorably Cute', 'softness': 'Soft and Snuggly'},
            {'name': 'Shadow', 'age': 3, 'cuteness': 'Majestic Cute', 'softness': 'Luxuriously Soft'},
            {'name': 'Whiskers', 'age': 1, 'cuteness': 'Playfully Cute', 'softness': 'Velvet Soft'},
        ]

        # Step 3: Populate the database with new kitten data
        self.stdout.write("Creating new kittens...")
        for kitten_data in kittens:
            Kitten.objects.create(**kitten_data)
            self.stdout.write(f"Added kitten: {kitten_data['name']}")
        
        self.stdout.write("Database successfully populated with new kittens.")