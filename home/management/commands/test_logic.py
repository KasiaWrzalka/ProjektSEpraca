from django.core.management.base import BaseCommand, CommandError
from django.db import connection, OperationalError
from home.models import Questions, AnswersFactors, Answers
import random

class Command(BaseCommand):
    help = 'Skrypt sprawdzający myślenie, pomagający uzupełnić pytania, faktors, conditions'

    # myślenie, skopiowane z logic.py
    def result(self, questions_answers, pytania):
        # print(questions_answers)

        wplywy = {}
        for i, j in questions_answers.items():
            for z in pytania:
                if z[0] == i:
                    for k in range(1, len(z)):
                        if z[1][0] == j:
                            if z[k][1] not in wplywy:
                                wplywy[z[k][1]] = z[k][2]
                            else:
                                wplywy[z[k][1]] += z[k][2]

        print(wplywy) # {'Introwersja': 2, 'Ekstrawersja': 2, 'Intuicja': 2, 'Poznanie': 2, 'Odczuwanie': 2, 'Myślenie': 2, 'Osądzanie': 1, 'Obserwacja': 1}
        odp = 'jesteś myślicielem'
        return odp

    def handle(self, *args, **options):
        print('***** START *****')
        # lista z pytaniami i ich wpływami na cechy osobowości -> do tabeli answersfactors
        pytania = [
            ['Czy lubisz spędzać czas w domu?', ['Tak', 'Introwersja', 1], ['Nie', 'Ekstrawersja', 1]],
            ['Czy w grupie osób najwięcej mówisz?', ['Tak', 'Ekstrawersja', 1], ['Nie', 'Introwersja', 1]],
            ['Lubisz być zaangażowany w pracę wymagającą aktywności i podejmowania szybkich działań?', ['Tak', 'Ekstrawersja', 1], ['Nie', 'Introwersja', 1]],
            ['Bardziej interesuje cię ogólna idea projektu, niż szczegóły jego realizacji?', ['Tak', 'Intuicja', 1], ['Nie', 'Poznanie', 1]],
            ['Wolisz raczej działać natychmiast, niż zastanawiać się nad wieloma rozwiązaniami?', ['Tak', 'Intuicja', 1], ['Nie', 'Poznanie', 1]],
            ['Zwykle z góry planujesz swoje działania?', ['Tak', 'Poznanie', 2], ['Nie', 'Intuicja', 1], ['Tak', 'Myślenie', 1]],
            ['Jesteś gotów pomagać ludziom nie oczekując niczego w zamian?', ['Tak', 'Odczuwanie', 1], ['Nie', 'Myślenie', 1]],
            ['Łatwo poddajesz się silnym emocjom?', ['Tak', 'Odczuwanie', 1], ['Nie', 'Myślenie', 1]],
            ['W nowym miejscu pracy szybko angażujesz się w życie biurowe?', ['Tak', 'Odczuwanie', 1], ['Nie', 'Myślenie', 1]],
            ['Robisz wszystko, by skończyć zadanie na czas?', ['Tak', 'Osądzanie', 1], ['Nie', 'Obserwacja', 1]],
            ['Niewielki stres nie zakłóca Twojej umiejętności relaksowania sie i koncentracji?', ['Tak', 'Obserwacja', 1], ['Nie', 'Osądzanie', 1]],
            ['Ostateczne terminy jawią ci się jako relatywne, nie zaś absolutne i ważne?', ['Tak', 'Obserwacja', 1], ['Nie', 'Osądzanie', 1]]
        ]
        #losujemy odpowiedzi każdego pytania
        test_answers = {}
        for pytanie in pytania:
            test_answers[pytanie[0]] = random.choice(['Tak', 'Nie'])

        # wprowadzamy do części myślenia def results
        z = self.result(test_answers, pytania)
        print('odpowiedź --------------------->', z)
        print('***** END *****')