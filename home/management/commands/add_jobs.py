from django.core.management.base import BaseCommand, CommandError
from django.db import connection, OperationalError

class Command(BaseCommand):
    help = 'Uzupełnia tabele Jobs'

    def handle(self, *args, **options):
        print('***** START *****')
        cursor = connection.cursor()

        MBTI_zawody = {
            'ESTJ': ["bibliotekarz", "farmaceuta", "informatyk", "koordynator projektu", "księgowy",
                                "kucharz", "menedżer", "nauczyciel", "naukowiec", "pracownik banku", "policjant",
                                "polityk", "prawnik", "sprzedawca", "żołnierz"],
                       'ESFJ': ["prawnik", "aktor", "pracownik banku", "duchowny", "farmaceuta", "fizjoterapeuta",
                                "księgowy", "lekarz", "menedżer", "nauczyciel", "pielęgniarka", "sprzedawca", "trener"],
                       'ESTP': ["aktor", "pracownik banku", "elektryk", "fizjoterapeuta", "fotograf", "kierowca",
                                "logistyk", "policjant", "pracownik budowlany", "przedsiębiorca",
                                "ratownik", "sportowiec", "sprzedawca", "strażak", "trener", "żołnierz"],
                       'ISFP': ["artysta", "naukowiec", "dekorator wnętrz", "fotograf", "fryzjer",
                                "kucharz", "lekarz", "malarz", "mechanik", "muzyk", "nauczyciel",
                                "psycholog", "ratownik", "stylista",  "trener", "weterynarz"],
                       'ENFJ': ["aktor", "doradca", "duchowny", "menedżer", "konsultant", "lekarz", "muzyk",
                                "nauczyciel", "naukowiec", "pisarz", "policjant", "polityk", "sprzedawca",
                                "psychiatra", "psycholog", "dziennikarz", "specjalista ds. pracowniczych",
                                "trener"],
                       'ENTJ': ["dziennikarz", "informatyk", "koordynator projektu", "menedżer", "muzyk", "naukowiec",
                                "pisarz", "planista", "polityk", "prawnik", "przedsiębiorca", "psycholog",
                                "specjalista ds. pracowniczych", "pracownik banku", "sprzedawca"],
                       'ENFP': ["aktor", "doradca", "duchowny", "dziennikarz", "konsultant", "malarz",
                                "menedżer", "muzyk", "nauczyciel", "naukowiec", "organizator imprez", "pisarz",
                                "polityk", "przedsiębiorca", "dekorator wnętrz", "psycholog", "psychiatra", "sprzedawca"],
                       'INFP': ["aktor", "artysta",  "dekorator wnętrz", "doradca", "duchowny", "dziennikarz",
                                "fizjoterapeuta", "konsultant", "koordynator projektu", "muzyk", "nauczyciel",
                                "naukowiec", "pisarz", "psychiatra", "psycholog", "specjalista ds. pracowniczych",
                                "trener", "tłumacz"],
                       'ENTP': ["aktor", "pracownik banku", "artysta", "doradca", "dziennikarz", "fotograf", "inżynier",
                                "koordynator projektu", "logistyk", "muzyk", "naukowiec", "organizator imprez",
                                "pisarz", "planista", "polityk", "prawnik", "informatyk", "przedsiębiorca",
                                "psychiatra", "psycholog", "sprzedawca"],
                       'ISTJ': ["bibliotekarz", "farmaceuta", "informatyk", "inżynier", "księgowy", "lekarz",
                                "logistyk", "lotnik", "nauczyciel", "mechanik", "menedżer", "policjant", "prawnik",
                                "informatyk", "przedsiębiorca", "rolnik", "żołnierz"],
                       'INTP': ["analityk", "archeolog", "architekt", "doradca",  "pracownik banku", "fotograf",
                                "informatyk", "przedsiębiorca", "muzyk", "naukowiec", "pisarz", "planista",
                                "prawnik", "informatyk", "tłumacz", "nauczyciel", "filmowiec"],
                       'INFJ': ["artysta", "bibliotekarz", "doradca", "duchowny", "dziennikarz", "filmowiec",
                                "fizjoterapeuta", "fotograf", "konsultant", "koordynator projektu", "lekarz", "muzyk",
                                "nauczyciel", "naukowiec", "prawnik", "pisarz", "psycholog"],
                       'ISFJ': [ "aktor", "bibliotekarz", "dekorator wnętrz", "doradca", "duchowny", "fizjoterapeuta",
                                 "księgowy", "lekarz", "menedżer", "muzyk", "nauczyciel", "pracownik budowlany",
                                 "przedsiębiorca", "psycholog", "rolnik", "trener", "weterynarz"],
                       'ISTP': [ "pracownik banku", "elektryk", "farmaceuta", "inżynier", "kierowca", "lotnik",
                                 "mechanik", "muzyk", "policjant", "pracownik budowlany", "prawnik", "informatyk",
                                 "przedsiębiorca", "ratownik", "rolnik", "informatyk", "sportowiec", "strażak", "żołnierz"],
                       'ESFP': ["aktor", "dekorator wnętrz", "doradca", "fotograf", "konsultant", "lekarz", "malarz",
                                "muzyk", "nauczyciel", "organizator imprez", "przedsiębiorca", "sprzedawca", "psycholog",
                                "ratownik", "stylista", "trener", "weterynarz"],
                       'INTJ': ["analityk", "architekt", "pracownik banku", "fotograf", "informatyk", "przedsiębiorca",
                                "inżynier", "koordynator projektu", "lekarz", "menedżer", "nauczyciel", "naukowiec",
                                "pisarz", "polityk", "planista", "informatyk", "psycholog", "prawnik"]}

        # zawody = set(val for dic in MBTI_zawody for val in dic.values())
        # print(zawody)
        # s = set(k for i, j in MBTI_zawody.items() for k in j)
        # z = {}
        # for i, j in MBTI_zawody.items():
        #     for k in j:
        #         if k not in z:
        #             z[k] = 1
        #         else:
        #             z[k] += 1
        # print(z)
        # print(s, len(s), type(s))
        # print(sorted(s))

        zawody = ['aktor', 'analityk', 'archeolog', 'architekt', 'artysta', 'bibliotekarz', 'dekorator wnętrz',
                  'doradca', 'duchowny', 'dziennikarz', 'elektryk', 'farmaceuta', 'filmowiec', 'fizjoterapeuta',
                  'fotograf', 'fryzjer', 'informatyk', 'inżynier', 'kierowca', 'konsultant', 'koordynator projektu',
                  'księgowy', 'kucharz', 'lekarz', 'logistyk', 'lotnik', 'malarz', 'mechanik', 'menedżer', 'muzyk',
                  'nauczyciel', 'naukowiec', 'organizator imprez', 'pielęgniarka', 'pisarz', 'planista', 'policjant',
                  'polityk', 'pracownik banku', 'pracownik budowlany', 'prawnik', 'przedsiębiorca', 'psychiatra',
                  'psycholog', 'ratownik', 'rolnik', 'specjalista ds. pracowniczych', 'sportowiec', 'sprzedawca',
                  'strażak', 'stylista', 'trener', 'tłumacz', 'weterynarz', 'żołnierz']

        cechy = ("Niezależność", "Atmosfera i kontakty społeczne",
             "Kierowanie innymi", "Dobre warunki finansowe",
             "Jasne cele i zadania", "Urozmaicenie",
             "Produktywność i wyzwania", "Uznanie, pochwały",
             "Rozwój osobisty", "Niski poziom stresu")

        # zawody_cechy = {}
        # for zawod in zawody:
        #     zawody_cechy[zawod] = {key: 1 for key in cechy}
        # print(zawody_cechy)

        # r = "SELECT `id`, `title` FROM `home_results`"
        # cursor.execute(r)
        # re = cursor.fetchall()
        # results = dict((y, x) for x, y in re)
        # print(results)

        zawody_cechy = {
                           'aktor': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 1, 'Urozmaicenie': 3, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 3, 'Rozwój osobisty': 3, 'Niski poziom stresu': 1},
                           'analityk': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 2, 'Dobre warunki finansowe': 3, 'Jasne cele i zadania': 1, 'Urozmaicenie': 3, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 2, 'Niski poziom stresu': 1},
                           'archeolog': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 1, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 2, 'Urozmaicenie': 3, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 3, 'Rozwój osobisty': 2, 'Niski poziom stresu': 2},
                           'architekt': {'Niezależność': 2, 'Atmosfera i kontakty społeczne': 2, 'Kierowanie innymi': 2, 'Dobre warunki finansowe': 3, 'Jasne cele i zadania': 3, 'Urozmaicenie': 3, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 1, 'Rozwój osobisty': 2, 'Niski poziom stresu': 2},
                           'artysta': {'Niezależność': 3, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 1, 'Jasne cele i zadania': 1, 'Urozmaicenie': 3, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 3, 'Rozwój osobisty': 3, 'Niski poziom stresu': 3},
            'bibliotekarz': {'Niezależność': 3, 'Atmosfera i kontakty społeczne': 1, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 1, 'Jasne cele i zadania': 3, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 1, 'Uznanie, pochwały': 1, 'Rozwój osobisty': 2, 'Niski poziom stresu': 3},
            'dekorator wnętrz': {'Niezależność': 2, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 1, 'Urozmaicenie': 3, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 2, 'Niski poziom stresu': 1},
            'doradca': {'Niezależność': 3, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 3, 'Dobre warunki finansowe': 3, 'Jasne cele i zadania': 2, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 2, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 2, 'Niski poziom stresu': 1},
            'duchowny': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 3, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 1, 'Uznanie, pochwały': 3, 'Rozwój osobisty': 1, 'Niski poziom stresu': 1},
            'dziennikarz': {'Niezależność': 2, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 1, 'Jasne cele i zadania': 2, 'Urozmaicenie': 3, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 3, 'Rozwój osobisty': 1, 'Niski poziom stresu': 1},
            'elektryk': {'Niezależność': 2, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 1, 'Niski poziom stresu': 1},
            'farmaceuta': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 2, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 1, 'Uznanie, pochwały': 1, 'Rozwój osobisty': 1, 'Niski poziom stresu': 2},
            'filmowiec': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 3, 'Dobre warunki finansowe': 3, 'Jasne cele i zadania': 2, 'Urozmaicenie': 2, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 3, 'Rozwój osobisty': 3, 'Niski poziom stresu': 1},
            'fizjoterapeuta': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 2, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 2, 'Niski poziom stresu': 3},
            'fotograf': {'Niezależność': 3, 'Atmosfera i kontakty społeczne': 2, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 1, 'Jasne cele i zadania': 3, 'Urozmaicenie': 2, 'Produktywność i wyzwania': 2, 'Uznanie, pochwały': 3, 'Rozwój osobisty': 3, 'Niski poziom stresu': 3},
            'fryzjer': {'Niezależność': 3, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 2, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 2, 'Produktywność i wyzwania': 2, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 2, 'Niski poziom stresu': 3},
            'informatyk': {'Niezależność': 2, 'Atmosfera i kontakty społeczne': 1, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 3, 'Jasne cele i zadania': 3, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 2, 'Uznanie, pochwały': 1, 'Rozwój osobisty': 3, 'Niski poziom stresu': 2},
            'inżynier': {'Niezależność': 2, 'Atmosfera i kontakty społeczne': 1, 'Kierowanie innymi': 2, 'Dobre warunki finansowe': 3, 'Jasne cele i zadania': 2, 'Urozmaicenie': 2, 'Produktywność i wyzwania': 2, 'Uznanie, pochwały': 1, 'Rozwój osobisty': 2, 'Niski poziom stresu': 2},
            'kierowca': {'Niezależność': 3, 'Atmosfera i kontakty społeczne': 2, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 1, 'Rozwój osobisty': 1, 'Niski poziom stresu': 2},
            'konsultant': {'Niezależność': 3, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 2, 'Urozmaicenie': 2, 'Produktywność i wyzwania': 2, 'Uznanie, pochwały': 3, 'Rozwój osobisty': 2, 'Niski poziom stresu': 2},
                           'koordynator projektu': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 3, 'Dobre warunki finansowe': 3, 'Jasne cele i zadania': 2, 'Urozmaicenie': 2, 'Produktywność i wyzwania': 2, 'Uznanie, pochwały': 3, 'Rozwój osobisty': 3, 'Niski poziom stresu': 2},
                           'księgowy': {'Niezależność': 2, 'Atmosfera i kontakty społeczne': 1, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 1, 'Rozwój osobisty': 2, 'Niski poziom stresu': 2},
                           'kucharz': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 1, 'Kierowanie innymi': 2, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 2, 'Niski poziom stresu': 2},
                           'lekarz': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 2, 'Kierowanie innymi': 3, 'Dobre warunki finansowe': 3, 'Jasne cele i zadania': 2, 'Urozmaicenie': 3, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 3, 'Rozwój osobisty': 3, 'Niski poziom stresu': 1},
                           'logistyk': {'Niezależność': 3, 'Atmosfera i kontakty społeczne': 1, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 2, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 2, 'Uznanie, pochwały': 1, 'Rozwój osobisty': 2, 'Niski poziom stresu': 2},
                           'lotnik': {'Niezależność': 3, 'Atmosfera i kontakty społeczne': 1, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 2, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 1, 'Uznanie, pochwały': 1, 'Rozwój osobisty': 1, 'Niski poziom stresu': 1},
                           'malarz': {'Niezależność': 3, 'Atmosfera i kontakty społeczne': 1, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 1, 'Jasne cele i zadania': 3, 'Urozmaicenie': 3, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 3, 'Rozwój osobisty': 3, 'Niski poziom stresu': 3},
                           'mechanik': {'Niezależność': 3, 'Atmosfera i kontakty społeczne': 2, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 1, 'Jasne cele i zadania': 3, 'Urozmaicenie': 2, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 2, 'Niski poziom stresu': 3},
                           'menedżer': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 3, 'Dobre warunki finansowe': 3, 'Jasne cele i zadania': 1, 'Urozmaicenie': 3, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 3, 'Rozwój osobisty': 3, 'Niski poziom stresu': 1},
                           'muzyk': {'Niezależność': 3, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 1, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 1, 'Uznanie, pochwały': 3, 'Rozwój osobisty': 2, 'Niski poziom stresu': 1},
                           'nauczyciel': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 2, 'Kierowanie innymi': 2, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 2, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 1, 'Niski poziom stresu': 2},
                           'naukowiec': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 1, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 3, 'Jasne cele i zadania': 2, 'Urozmaicenie': 3, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 3, 'Niski poziom stresu': 2},
                           'organizator imprez': {'Niezależność': 3, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 3, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 2, 'Produktywność i wyzwania': 2, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 2, 'Niski poziom stresu': 1},
                           'pielęgniarka': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 1, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 2, 'Produktywność i wyzwania': 2, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 2, 'Niski poziom stresu': 1},
                           'pisarz': {'Niezależność': 3, 'Atmosfera i kontakty społeczne': 1, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 2, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 2, 'Niski poziom stresu': 3},
                           'planista': {'Niezależność': 2, 'Atmosfera i kontakty społeczne': 2, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 2, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 1, 'Rozwój osobisty': 2, 'Niski poziom stresu': 2},
                           'policjant': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 2, 'Kierowanie innymi': 3, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 2, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 2, 'Niski poziom stresu': 1},
                           'polityk': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 3, 'Dobre warunki finansowe': 3, 'Jasne cele i zadania': 2, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 1, 'Uznanie, pochwały': 3, 'Rozwój osobisty': 3, 'Niski poziom stresu': 1},
                           'pracownik banku': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 2, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 1, 'Uznanie, pochwały': 1, 'Rozwój osobisty': 2, 'Niski poziom stresu': 1},
                           'pracownik budowlany': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 1, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 1, 'Jasne cele i zadania': 3, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 1, 'Rozwój osobisty': 1, 'Niski poziom stresu': 3},
                           'prawnik': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 2, 'Dobre warunki finansowe': 3, 'Jasne cele i zadania': 1, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 2, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 2, 'Niski poziom stresu': 2},
                           'przedsiębiorca': {'Niezależność': 3, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 3, 'Dobre warunki finansowe': 3, 'Jasne cele i zadania': 1, 'Urozmaicenie': 3, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 2, 'Niski poziom stresu': 2},
                           'psychiatra': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 2, 'Kierowanie innymi': 3, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 2, 'Urozmaicenie': 2, 'Produktywność i wyzwania': 2, 'Uznanie, pochwały': 1, 'Rozwój osobisty': 1, 'Niski poziom stresu': 1},
                           'psycholog': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 2, 'Kierowanie innymi': 2, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 2, 'Urozmaicenie': 2, 'Produktywność i wyzwania': 2, 'Uznanie, pochwały': 1, 'Rozwój osobisty': 1, 'Niski poziom stresu': 2},
                           'ratownik': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 2, 'Kierowanie innymi': 2, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 3, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 1, 'Niski poziom stresu': 1},
                           'rolnik': {'Niezależność': 3, 'Atmosfera i kontakty społeczne': 1, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 1, 'Jasne cele i zadania': 3, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 1, 'Rozwój osobisty': 1, 'Niski poziom stresu': 3},
                           'specjalista ds. pracowniczych': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 2, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 2, 'Urozmaicenie': 2, 'Produktywność i wyzwania': 2, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 1, 'Niski poziom stresu': 1},
                           'sportowiec': {'Niezależność': 3, 'Atmosfera i kontakty społeczne': 1, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 3, 'Rozwój osobisty': 3, 'Niski poziom stresu': 1},
                           'sprzedawca': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 2, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 1, 'Uznanie, pochwały': 1, 'Rozwój osobisty': 1, 'Niski poziom stresu': 3},
            'strażak': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 2, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 2, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 2, 'Niski poziom stresu': 1},
            'stylista': {'Niezależność': 2, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 2, 'Produktywność i wyzwania': 2, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 2, 'Niski poziom stresu': 3},
            'trener': {'Niezależność': 3, 'Atmosfera i kontakty społeczne': 2, 'Kierowanie innymi': 3, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 2, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 3, 'Niski poziom stresu': 3},
                           'tłumacz': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 2, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 1, 'Produktywność i wyzwania': 2, 'Uznanie, pochwały': 1, 'Rozwój osobisty': 3, 'Niski poziom stresu': 3},
            'weterynarz': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 2, 'Kierowanie innymi': 2, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 3, 'Produktywność i wyzwania': 2, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 3, 'Niski poziom stresu': 2},
            'żołnierz': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 2, 'Kierowanie innymi': 1, 'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 3, 'Urozmaicenie': 2, 'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 2, 'Rozwój osobisty': 3, 'Niski poziom stresu': 1}}

        # 'aktor': {'Niezależność': 1, 'Atmosfera i kontakty społeczne': 3, 'Kierowanie innymi': 1,
        #           'Dobre warunki finansowe': 2, 'Jasne cele i zadania': 1, 'Urozmaicenie': 3,
        #           'Produktywność i wyzwania': 3, 'Uznanie, pochwały': 3, 'Rozwój osobisty': 3,
        #           'Niski poziom stresu': 1}
        # for i, j in zawody_cechy.items():
        #     sql = "INSERT INTO `sonji1_kasia`.`home_jobs` (`id`, `name`, `autonomia`, `atmosfera`, `kierowanie`, " \
        #           "`finanse`, `zadania`, `urozmaicenie`, `wyzwania`, `uznanie`, `rozwój`, `stres`) " \
        #           "VALUES (NULL, '{}', '{}', '{}', " \
        #           "'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(i,
        #                                                                    j['Niezależność'],
        #                                                                    j['Atmosfera i kontakty społeczne'],
        #                                                                    j['Kierowanie innymi'],
        #                                                                    j['Dobre warunki finansowe'],
        #                                                                    j['Jasne cele i zadania'],
        #                                                                    j['Urozmaicenie'],
        #                                                                    j['Produktywność i wyzwania'],
        #                                                                    j['Uznanie, pochwały'],
        #                                                                    j['Rozwój osobisty'],
        #                                                                    j['Niski poziom stresu'])
        #
        #     print(sql)
            # cursor.execute(sql)

        print(MBTI_zawody)

        r = "SELECT `id`, `title` FROM `home_results`"
        cursor.execute(r)
        re = cursor.fetchall()
        results = dict((y, x) for x, y in re)
        print(results)
        # {'ESTJ': 6, 'ESFJ': 7, 'ESTP': 8, 'ISFP': 9, 'ENFJ': 10, 'ENTJ': 11, 'ENFP': 12, 'INFP': 13, 'ENTP': 14,
        #  'ISTJ': 15, 'INTP': 16, 'INFJ': 17, 'ISFJ': 18, 'ISTP': 19, 'ESFP': 20, 'INTJ': 21}

        j = "SELECT `id`, `name` FROM `home_jobs`"
        cursor.execute(j)
        jo = cursor.fetchall()
        jobs = dict((y, x) for x, y in jo)
        print(jobs)

        for i, j in MBTI_zawody.items():
            for k in j:
                sql1 = "INSERT INTO `sonji1_kasia`.`home_resultsjobs` (`id`, `result_id`, `job_id`) VALUES (NULL, '{}', '{}')".format(results[i], jobs[k])
                print(sql1)
                # cursor.execute(sql1)


        print('***** END *****')