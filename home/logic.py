from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from .models import Questions

class MyQuestions(object):

    def all_questions():
        questions = Questions.objects.all()
        return questions
