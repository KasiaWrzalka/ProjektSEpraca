from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from .models import Questions, AnswersFactors, Answers, Results
import random

class MyQuestions(object):

    def all_questions(test_id):
        """
        :return: wszystkie pytania z danego testu
        """
        questions = Questions.objects.filter(test=test_id)
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