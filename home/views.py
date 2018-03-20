from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from .models import Answers
from .logic import MyQuestions

def IndexView(request):
    return render_to_response('home/index.html')

def TestMbtiView(request):
    q = MyQuestions.all_questions(1)
    question_answers_dict = {}
    for i in q:
        question_answers_dict[i] = [z for z in Answers.objects.filter(question=i.id)]
    return render(request, 'home/test.html', {'questions': q, 'question_answers': question_answers_dict})

@csrf_exempt
def vote(request, test_id):
    questions = MyQuestions.all_questions(1)
    questions_answers = dict(request.POST)
    del questions_answers['csrfmiddlewaretoken']
    try:
        if len(questions) == len(request.POST) - 1:
            odp = u"Super! Uzupełniłeś wszystkie pytania. Twoja odpowiedź to: " + MyQuestions.result(questions_answers)
        else:
            odp = u"Uzupełnij wszystkie pytania. Wróć do testu."
        return render(request, 'home/results.html', {'odp': odp})
    except KeyError:
        print(u'błąd')
        return render(request, 'home/results.html', {'odp': "Wysłałeś pustą odpowiedź. Sprójbuj jeszcze raz!."})

