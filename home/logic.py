from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from .models import Questions, AnswersFactors, Conditions, Factors

class MyQuestions(object):

    def all_questions(test_id):
        questions = Questions.objects.filter(test=test_id)
        return questions

    def result(questions_answers):
        print(questions_answers)
        # zliczamy ile zdobyliśmy do pojedyńczych osobowości
        a = []
        for k, v in questions_answers.items():
            for i in v:
                a.append(i)
        answers = AnswersFactors.objects.filter(answer_id__in=a)
        odp = ''
        rozw_dict = {}
        for i in answers:
            print(i.impact, i.factor.title)
            odp += ' ' + str(i.impact) + ' ' + str(i.factor.title)
            if i.factor.id in rozw_dict:
                rozw_dict[i.factor.id] += i.impact
            else:
                rozw_dict[i.factor.id] = i.impact
        print(rozw_dict)
        odp += str(rozw_dict)

        # result

        return odp