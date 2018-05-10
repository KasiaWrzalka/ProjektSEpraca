from django.core.management.base import BaseCommand, CommandError
from django.db import connection, OperationalError

class Command(BaseCommand):
    help = 'Uzupełnia tabele Questions i tabele Answers'

    def handle(self, *args, **options):
        print('***** START *****')
        cursor = connection.cursor()

        pytania = [
            ['Czy lubisz spędzać czas w domu?', ['Tak', 'Introwersja', 1], ['Nie', 'Ekstrawersja', 1]],
            ['Często zastanawiasz się nad sensem życia?', ['Tak', 'Introwersja', 3], ['Nie', 'Ekstrawersja', 2]],
            ['Bardziej przemawiają do mnie sprawdzone, wypróbowane rozwiązania niż twórcze nowatorskie pomysły.', ['Tak', 'Poznanie', 2], ['Nie', 'Intuicja', 2], ['Tak', 'Ekstrawersja', 1]],
            ['Wolisz pracę zespołową niż indywidualną.', ['Nie', 'Introwersja', 1], ['Tak', 'Ekstrawersja', 1], ['Tak', 'Odczuwanie', 1]],
            ['Raczej korzystasz z rad innych ludzi niż ich udzielasz.', ['Nie', 'Osądzanie', 3], ['Tak', 'Obserwacja', 3], ['Tak', 'Introwersja', 1], ['Nie', 'Ekstrawersja', 1]],
            ['Aby zachować dobre relacje z ludźmi, często ustępuje innym, nawet jeśli nie jest mi to na ręke.', ['Tak', 'Odczuwanie', 3], ['Nie', 'Myślenie', 3], ['Nie', 'Myślenie', 1]],
            ['Najlepiej odpoczywasz wśród wielu ludzi, w miejscu w którym zawsze coś się dzieje?', ['Nie', 'Introwersja', 2], ['Tak', 'Ekstrawersja', 1], ['Tak', 'Obserwacja', 1]],
            ['Nie lubisz na sztywno planować dnia, nagłe zmiany są ciekawym urozmaiceniem?', ['Nie', 'Osądzanie', 2], ['Tak', 'Obserwacja', 3]],
            ['Odpowiadają ci książki napisane rzeczowo, skupiające się na faktach.', ['Tak', 'Poznanie', 3]],
            ['Czy w grupie osób najwięcej mówisz?', ['Tak', 'Ekstrawersja', 1], ['Nie', 'Introwersja', 1]],
            ['Lubisz być zaangażowany w pracę wymagającą aktywności i podejmowania szybkich niezaplanowanych działań?', ['Tak', 'Ekstrawersja', 1], ['Nie', 'Introwersja', 1], ['Tak', 'Obserwacja', 2]],
            ['W nowym miejscu pracy szybko angażujesz się w życie biurowe?', ['Tak', 'Odczuwanie', 1], ['Nie', 'Myślenie', 1], ['Tak', 'Ekstrawersja', 2]],
            ['Bardziej interesuje cię ogólna idea projektu, niż szczegóły jego realizacji?', ['Tak', 'Intuicja', 1], ['Nie', 'Poznanie', 1], ['Nie', 'Osądzanie', 2]],
            ['Wolisz raczej działać natychmiast, niż zastanawiać się nad wieloma rozwiązaniami?', ['Tak', 'Intuicja', 3], ['Nie', 'Poznanie', 3]],
            ['Zwykle z góry planujesz swoje działania?', ['Tak', 'Poznanie', 2], ['Nie', 'Intuicja', 1], ['Tak', 'Myślenie', 1]],
            ['Jesteś gotów pomagać ludziom nie oczekując niczego w zamian?', ['Tak', 'Odczuwanie', 1], ['Nie', 'Myślenie', 1]],
            ['Łatwo poddajesz się silnym emocjom?', ['Tak', 'Odczuwanie', 1], ['Nie', 'Myślenie', 1]],
            ['Robisz wszystko, by skończyć zadanie na czas?', ['Tak', 'Osądzanie', 1], ['Nie', 'Obserwacja', 1]],
            ['Niewielki stres nie zakłóca Twojej umiejętności relaksowania sie i koncentracji?', ['Tak', 'Obserwacja', 2], ['Nie', 'Osądzanie', 2]],
            ['Ostateczne terminy jawią ci się jako relatywne, nie zaś absolutne i ważne?', ['Tak', 'Obserwacja', 3], ['Nie', 'Osądzanie', 2]],
            ['Rozwiązując jakiś problem, staram się zachować obiektywizm, nawet kosztem sympatii ludzi.', ['Tak', 'Myślenie', 2], ['Nie', 'Odczuwanie', 1]],
            ['Wolisz wykonywać nowe zadania niż już ci znane?', ['Tak', 'Intuicja', 3], ['Nie', 'Poznanie', 3], ['Tak', 'Obserwacja', 1]],
            ['Łatwo się rozpraszasz, nie potrafisz się skupić przez dłuższy czas na jednej rzeczy, robisz częste przerwy w pracy?', ['Nie', 'Introwersja', 1], ['Tak', 'Ekstrawersja', 1], ['Tak', 'Obserwacja', 1]],
            ['Bardziej denerwują mnie marzyciele, myślący o przyszłości niż realiści myślący o czasie obecnym.', ['Nie', 'Intuicja', 1], ['Tak', 'Poznanie', 1]],
            ['Wolę osoby oschłe ale logiczne bardziej od osób chaotycznych ale sympatycznych. ', ['Tak', 'Myślenie', 2], ['Nie', 'Odczuwanie', 1]],
            ['Krytyka, nawet jeśli obiektywna, czyni więcej złego niż dobrego. ', ['Tak', 'Odczuwanie', 3], ['Nie', 'Myślenie', 1], ['Nie', 'Osądzanie', 1]],
            ['Lubię zapisywać terminy spotkań, wyjazdów, spraw do załatwienia. ', ['Tak', 'Poznanie', 1], ['Nie', 'Obserwacja', 1], ['Tak', 'Osądzanie', 1]],
            ['Wolę zysk mniejszy ale szybki od czasochłonnego ale wysokiego.', ['Tak', 'Poznanie', 2], ['Nie', 'Intuicja', 1]],
            ['Nie tracę czasu na przygotowywanie planu, jak najszybciej przystępuje do pracy.', ['Nie', 'Obserwacja', 1], ['Tak', 'Osądzanie', 1]],
            ['Zwykle jestem jednym z pierwszych, którzy dzwonią, aby pocieszyć kogoś, kto znalazł się w trudnej sytuacji.', ['Tak', 'Odczuwanie', 2], ['Tak', 'Ekstrawersja', 1], ['Nie', 'Myślenie', 1]],
            ['Mając nowe urządznie pierwsze co robie to dokładnie zapoznaję się z instrukcją', ['Tak', 'Poznanie', 2], ['Nie', 'Intuicja', 3], ['Tak', 'Osądzanie', 1]],
            ['Po ukończeniu ważnego zadania największą satysfakcję sprawia mi pochwała i uznanie innych ludzi. ', ['Tak', 'Odczuwanie', 3], ['Nie', 'Myślenie', 1], ['Nie', 'Introwersja', 1], ['Nie', 'Osądzanie', 1]],
            ['Często opowiadam innym o moich przeżyciach?', ['Nie', 'Introwersja', 3], ['Tak', 'Ekstrawersja', 3]],
            ['Potrafię płakać na filmach.', ['Tak', 'Odczuwanie', 2], ['Nie', 'Myślenie', 1]],
            ['Zdarza mi się wchodzić w słowo, przerywać innym', ['Tak', 'Odczuwanie', 2], ['Nie', 'Introwersja', 3], ['Tak', 'Ekstrawersja', 3]],
            ['Do powierzonych zadań lubię konkretną instrukcję niż możliwość decydowania o rozwiązaniu.', ['Tak', 'Poznanie', 2], ['Nie', 'Intuicja', 1]],
            ['Pytany o coś odpowiadam natychmiast bez chwili na zastanowienie.', ['Tak', 'Ekstrawersja', 1], ['Tak', 'Odczuwanie', 2], ['Nie', 'Myślenie', 1]],
            ['Lubię życie pełne zmian i niespodzianek, nudzi mnie życie wg schematów/planów.', ['Tak', 'Obserwacja', 3], ['Nie', 'Osądzanie', 2]],
            ['Gorsza jest decyzja nielogiczna niż sprawiająca przykrość wielu ludziom.', ['Nie', 'Odczuwanie', 2], ['Tak', 'Myślenie', 1]],
            ['Poszukując ofert pracy ważniejsze są obecne oferowane warunki zatrudnienia od przyszłości, rozwoju danego stanowiska.', ['Tak', 'Poznanie', 2], ['Nie', 'Intuicja', 1]],
            ['Zazwyczaj jestem dobrze przygotowany, nie musze improwizować.', ['Nie', 'Obserwacja', 3], ['Tak', 'Osądzanie', 2], ['Tak', 'Introwersja', 1]],
            ['Szukając współpracownika ważniejsze są kwalifikacje i zdolności od osobowości.', ['Nie', 'Odczuwanie', 2], ['Tak', 'Myślenie', 2], ['Tak', 'Ekstrawersja', 1]],
            ['Czy jesteś punktualny, nie spóźniasz się?', ['Nie', 'Obserwacja', 2], ['Tak', 'Osądzanie', 3]],
            ['Lubisz być w centrum uwagi, dodaje ci to sił?', ['Nie', 'Introwersja', 4], ['Tak', 'Ekstrawersja', 4]],
            ['Często zwlekasz z podjęciem decyzji?', ['Nie', 'Obserwacja', 2], ['Tak', 'Osądzanie', 3]],
            ['Jesteś raczej bezpośredni niż delikatny?', ['Nie', 'Odczuwanie', 2], ['Tak', 'Myślenie', 2]],
            ['Wolisz rozpoczynać nowe zadanie niż kończyć pracę nad zadaniem?', ['Tak', 'Obserwacja', 2], ['Nie', 'Osądzanie', 2]],
            ['Przed zakończeniem ankiety, testu, sprawdzianu sprawdzasz wszystkie swoje dane i odpowiedzi?', ['Tak', 'Poznanie', 3], ['Nie', 'Intuicja', 2], ['Tak', 'Osądzanie', 1]]
        ]

        f = "SELECT id, title FROM `home_factors`"
        cursor.execute(f)
        fa = cursor.fetchall()
        factors = dict((y, x) for x, y in fa)
        print(factors)

        for i in pytania:
            sql = u"INSERT INTO `sonji1_kasia`.`home_questions` (`id`, `test_id`, `title`) VALUES (NULL, '1', '{}')".format(i[0])
            # cursor.execute(sql)
            print('DODANO PYTANIE', sql)
            py = "SELECT * FROM `home_questions` WHERE `title` LIKE '{}'".format(i[0])
            cursor.execute(py)
            pyt = cursor.fetchall()
            print('DANE PYTANIA', pyt)

            if len(pyt) > 0:
                sq2 = "INSERT INTO `sonji1_kasia`.`home_answers` (`id`, `question_id`, `value`) VALUES (NULL, '{}', 'Tak'), (NULL, '{}', 'Nie')".format(
                    pyt[0][0], pyt[0][0])
                # cursor.execute(sq2)
                print('ODPOWIEDZI DO PYTANIA', sq2)
                for j in range(1, len(i)):
                    sq3 = """SELECT `id` FROM `home_answers` WHERE `question_id` = {} AND `value` LIKE '{}'""".format(
                        pyt[0][0], i[j][0])
                    cursor.execute(sq3)
                    sq3_answer = cursor.fetchall()
                    if len(sq3_answer) > 0:
                        sq4 = "INSERT INTO `sonji1_kasia`.`home_answersfactors` (`id`, `factor_id`, `answer_id`, `impact`) VALUES (NULL, '{}', '{}', '{}')".format(factors[i[j][1]], sq3_answer[0][0], i[j][2])
                        # cursor.execute(sq4)
                        print('DODANO WAGI ODPOWIEDZI', sq4)
            print('*'*30)


        # cursor.execute(sql)
        cursor.close()
        print('***** END *****')