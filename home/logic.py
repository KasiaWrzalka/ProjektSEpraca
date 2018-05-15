from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from .models import Questions, AnswersFactors, Answers, Results, Jobs
import random
import operator

class MyQuestions(object):

    def all_questions(test_id):
        """
        :return: wszystkie pytania z danego testu
        """
        questions = Questions.objects.filter(test=test_id)
        return questions

    def random_10_questions(test_id):
        """
        :return: 10 pytań z danego testu
        """
        count = Questions.objects.filter(test=test_id).count()
        slice = random.random() * (count - 3)
        random_10_questions = Questions.objects.filter(test=test_id)[slice: slice + 3]
        return random_10_questions

    def result(questions_answers):
        questions_answers2 = {}
        for k, v in questions_answers.items():
            questions_answers2[Questions.objects.get(id=k)] = Answers.objects.get(id=v[0])

        wplywy = {}
        for i, j in questions_answers2.items():
            for k in j.answersfactors_set.all():
                if k.factor.title not in wplywy:
                    wplywy[k.factor.title] = k.impact
                else:
                    wplywy[k.factor.title] += k.impact

        result = ''
        if 'Introwersja' not in wplywy or ('Ekstrawersja' in wplywy and wplywy['Ekstrawersja'] > wplywy['Introwersja']):
            result += 'E'
        else:
            result += 'I'
        if 'Intuicja' not in wplywy or ('Poznanie' in wplywy and wplywy['Poznanie'] > wplywy['Intuicja']):
            result += 'S'
        else:
            result += 'N'
        if 'Odczuwanie' not in wplywy or ('Myślenie' in wplywy and wplywy['Myślenie'] > wplywy['Odczuwanie']):
            result += 'F'
        else:
            result += 'T'
        if 'Obserwacja' not in wplywy or ('Osądzanie' in wplywy and wplywy['Osądzanie'] > wplywy['Obserwacja']):
            result += 'J'
        else:
            result += 'P'
        result = Results.objects.get(title=result)
        name = result.name
        title = result.title
        description = result.description
        jobs = [i.job.name for i in result.resultsjobs_set.all()]
        return (name, title, description, jobs)

    def result_job(questions_answers, title):
        questions_answers2 = {}
        for k, v in questions_answers.items():
            questions_answers2[Questions.objects.get(id=k)] = Answers.objects.get(id=v[0])

        result = Results.objects.get(title=title).resultsjobs_set.all()
        wynik = {}
        for i in result:
            wynik[i.job.name] = 0
        for i, j in questions_answers2.items():
            if str(j) == "2":
                for k in result:
                    if i.title == "Niezależność":
                        if k.job.autonomia == 0:
                            wynik[str(k.job.name)] -= 1
                        elif k.job.autonomia == 1:
                            wynik[str(k.job.name)] += 1
                    elif i.title == "Atmosfera i kontakty społeczne":
                        if k.job.atmosfera == 0:
                            wynik[str(k.job.name)] -= 1
                        elif k.job.atmosfera == 1:
                            wynik[str(k.job.name)] += 1
                    elif i.title == "Kierowanie innymi":
                        if k.job.kierowanie == 0:
                            wynik[str(k.job.name)] -= 1
                        elif k.job.kierowanie == 1:
                            wynik[str(k.job.name)] += 1
                    elif i.title == "Dobre warunki finansowe":
                        if k.job.finanse == 0:
                            wynik[str(k.job.name)] -= 1
                        elif k.job.finanse == 1:
                            wynik[str(k.job.name)] += 1
                    elif i.title == "Jasne cele i zadania":
                        if k.job.zadania == 0:
                            wynik[str(k.job.name)] -= 1
                        elif k.job.zadania == 1:
                            wynik[str(k.job.name)] += 1
                    elif i.title == "Urozmaicenie":
                        if k.job.urozmaicenie == 0:
                            wynik[str(k.job.name)] -= 1
                        elif k.job.urozmaicenie == 1:
                            wynik[str(k.job.name)] += 1
                    elif i.title == "Produktywność i wyzwania":
                        if k.job.wyzwania == 0:
                            wynik[str(k.job.name)] -= 1
                        elif k.job.wyzwania == 1:
                            wynik[str(k.job.name)] += 1
                    elif i.title == "Uznanie, pochwały":
                        if k.job.uznanie == 0:
                            wynik[str(k.job.name)] -= 1
                        elif k.job.uznanie == 1:
                            wynik[str(k.job.name)] += 1
                    elif i.title == "Rozwój osobisty":
                        if k.job.rozwoj == 0:
                            wynik[str(k.job.name)] -= 1
                        elif k.job.rozwoj == 1:
                            wynik[str(k.job.name)] += 1
                    elif i.title == "Niski poziom stresu":
                        if k.job.stres == 0:
                            wynik[str(k.job.name)] -= 1
                        elif k.job.stres == 1:
                            wynik[str(k.job.name)] += 1
            elif str(j) == "3":
                for k in result:
                    if i.title == "Niezależność":
                        if k.job.autonomia == 0:
                            wynik[str(k.job.name)] -= 2
                        elif k.job.autonomia == 1:
                            wynik[str(k.job.name)] += 2
                    elif i.title == "Atmosfera i kontakty społeczne":
                        if k.job.atmosfera == 0:
                            wynik[str(k.job.name)] -= 2
                        elif k.job.atmosfera == 1:
                            wynik[str(k.job.name)] += 2
                    elif i.title == "Kierowanie innymi":
                        if k.job.kierowanie == 0:
                            wynik[str(k.job.name)] -= 2
                        elif k.job.kierowanie == 1:
                            wynik[str(k.job.name)] += 2
                    elif i.title == "Dobre warunki finansowe":
                        if k.job.finanse == 0:
                            wynik[str(k.job.name)] -= 2
                        elif k.job.finanse == 1:
                            wynik[str(k.job.name)] += 2
                    elif i.title == "Jasne cele i zadania":
                        if k.job.zadania == 0:
                            wynik[str(k.job.name)] -= 2
                        elif k.job.zadania == 1:
                            wynik[str(k.job.name)] += 2
                    elif i.title == "Urozmaicenie":
                        if k.job.urozmaicenie == 0:
                            wynik[str(k.job.name)] -= 2
                        elif k.job.urozmaicenie == 1:
                            wynik[str(k.job.name)] += 2
                    elif i.title == "Produktywność i wyzwania":
                        if k.job.wyzwania == 0:
                            wynik[str(k.job.name)] -= 2
                        elif k.job.wyzwania == 1:
                            wynik[str(k.job.name)] += 2
                    elif i.title == "Uznanie, pochwały":
                        if k.job.uznanie == 0:
                            wynik[str(k.job.name)] -= 2
                        elif k.job.uznanie == 1:
                            wynik[str(k.job.name)] += 2
                    elif i.title == "Rozwój osobisty":
                        if k.job.rozwoj == 0:
                            wynik[str(k.job.name)] -= 2
                        elif k.job.rozwoj == 1:
                            wynik[str(k.job.name)] += 2
                    elif i.title == "Niski poziom stresu":
                        if k.job.stres == 0:
                            wynik[str(k.job.name)] -= 2
                        elif k.job.stres == 1:
                            wynik[str(k.job.name)] += 2

        highest = max(wynik.values())
        odp = [k for k, v in wynik.items() if v == highest]

        return odp