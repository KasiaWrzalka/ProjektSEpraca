from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from .models import Answers
from .logic import MyQuestions

def IndexView(request):
    return render_to_response('home/index.html')

def TestMbtiView(request):
    """
    :return: oddaje do html pytania i ich odpowiedzi
    """
    # q = MyQuestions.all_questions(1)
    q = MyQuestions.random_10_questions(1)
    question_answers_dict = {}
    for i in q:
        question_answers_dict[i] = [z for z in Answers.objects.filter(question=i.id)]
    return render(request, 'home/test.html', {'questions': q, 'question_answers': question_answers_dict})

def TestPropertiesView(request, title):
    """
    :return: oddaje do html pytania i ich odpowiedzi
    """
    q = MyQuestions.all_questions(2)
    question_answers_dict = {}
    for i in q:
        question_answers_dict[i] = [z for z in Answers.objects.filter(question=i.id)]
    return render(request, 'home/properties.html', {'questions': q, 'question_answers': question_answers_dict})


@csrf_exempt
def vote(request, test_id):
    """
    :return: dostaje odpowiedzi użytkownika i zwraca odpowiedź
    """
    print('akuku')
    if test_id == 1:
        questions = MyQuestions.random_10_questions(1)
        questions_answers = dict(request.POST)
        del questions_answers['csrfmiddlewaretoken']
        try:
            if len(questions) == len(request.POST) - 1:
                odp = MyQuestions.result(questions_answers)
                return render(request, 'home/results.html', {'name': odp[0], 'title': odp[1], 'description': odp[2]})
            else:
                odp = u"Uzupełnij wszystkie pytania. Wróć do testu."
                return render(request, 'home/results.html', {'name': odp})
        except KeyError:
            print(u'błąd')
            return render(request, 'home/results.html', {'odp': "Wysłałeś pustą odpowiedź. Sprójbuj jeszcze raz!."})
    elif test_id == 2:
        return render(request, 'home/result_job.html', {'name': 'ostateczne rozwiazanie'})
