from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from .models import Questions, AnswersFactors, Answers

class MyQuestions(object):

    def all_questions(test_id):
        questions = Questions.objects.filter(test=test_id)
        return questions

    def result(questions_answers):
        print(questions_answers)
        # chce tylko oodpowiedzi na razie
        a = []
        for k, v in questions_answers.items():
            for i in v:
                a.append(i)
        answers = Answers.objects.filter(id__in=a)
        odp = ''
        for i in answers:
            for j in i.answersfactors_set.all():
                print(j.impact, j.factor)
                # print(i.answersfactors_set.impact, i.factor.title)
                # odp += ' ' + str(i.impact) + ' ' + str(i.factor.title)
        return odp