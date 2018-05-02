from django.core.management.base import BaseCommand, CommandError
from django.db import connection, OperationalError

class Command(BaseCommand):
    help = 'Skrypt sprawdzający myślenie, pomagający uzupełnić pytania, faktors, conditions'

    def handle(self, *args, **options):
        print('***** START *****')
        # tupla z pytaniami i ich wpływami na cechy osobowości
        pytania = [
            ('Czy lubisz spędzać czas w domu?', ('Tak', 'Introwersja', 1), ('Nie', 'Ekstawersja', 1)),
            ('Czy w grupie osób najwięcej mówisz?', ('Tak', 'Ekstrawersja', 1), ('Nie', 'Introwersja', 1)),
            ('Lubisz być zaangażowany w pracę wymagającą aktywności i podejmowania szybkich działań?', ('Tak', 'Ekstrawersja', 1), ('Nie', 'Introwersja', 1)),
            ('Bardziej interesuje cię ogólna idea projektu, niż szczegóły jego realizacji?', ('Tak', 'Intuicja', 1), ('Nie', 'Poznanie', 1)),
            ('Wolisz raczej działać natychmiast, niż zastanawiać się nad wieloma rozwiązaniami?', ('Tak', 'Intuicja', 1), ('Nie', 'Poznanie', 1)),
            ('Zwykle z góry planujesz swoje działania?', ('Tak', 'Poznanie', 1), ('Nie', 'Intuicja', 1)),
            ('Jesteś gotów pomagać ludziom, nie oczekując niczego w zamian?', ('Tak', 'Odczuwanie', 1), ('Nie', 'Myślenie', 1)),
            ('Łatwo poddajesz się silnym emocjom?', ('Tak', 'Odczuwanie', 1), ('Nie', 'Myślenie', 1)),
            ('W nowym miejscu pracy szybko angażujesz się w życie biurowe?', ('Tak', 'Odczuwanie', 1), ('Nie', 'Myślenie', 1)),
            ('Robisz wszystko, by skończyć zadanie na czas?', ('Tak', 'Osądzanie', 1), ('Nie', 'Obserwacja', 1)),
            ('Niewielki stres nie zakłóca Twojej umiejętności relaksowania sie i koncentracji?', ('Tak', 'Obserwacja', 1), ('Nie', 'Osądzanie', 1)),
            ('Ostateczne terminy jawią ci się jako relatywne, nie zaś absolutne i ważne?', ('Tak', 'Obserwacja', 1), ('Nie', 'Osądzanie', 1))
        ]
        print(pytania)
        print('***** END *****')