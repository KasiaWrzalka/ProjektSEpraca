from django.core.management.base import BaseCommand, CommandError
from django.db import connection, OperationalError

class Command(BaseCommand):
    help = 'Skrypt sprawdzający myślenie, pomagający uzupełnić pytania, faktors, conditions'

    def handle(self, *args, **options):
        print('***** START *****')
        # tupla z pytaniami i ich wpływami na cechy osobowości
        pytania = [
            ('Czy lubisz spędzać czas w domu?', {'Tak': 'Introwersja', 'Nie': 'Ekstawersja'}),
            ('Czy w grupie osób najwięcej mówisz?', {'Tak': 'Ekstrawersja', 'Nie': 'Introwersja'}),
            ('Niewielki stres nie zakłóca Twojej umiejętności relaksowania sie i koncentracji?', {'Tak': 'Introwersja', 'Nie': 'Ekstawersja'})
        ]
        print(pytania)
        print('***** END *****')