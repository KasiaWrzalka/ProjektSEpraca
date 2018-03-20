from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from .models import Questions

class MyQuestions(object):

    def all_questions(test_id):
        questions = Questions.objects.filter(test=test_id)
        return questions

    def result(questions_answers):
        print(questions_answers)
        odp = 'introwertyk'
        return odp