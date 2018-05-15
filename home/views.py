from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from .models import Answers, Results
from .logic import MyQuestions

def IndexView(request):
    return render_to_response('home/index.html')

def TestMbtiView(request):
    """
    :return: oddaje do html pytania i ich odpowiedzi
    """
    # q = MyQuestions.all_questions(1)
    q = MyQuestions.all_questions(1)
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
    return render(request, 'home/properties.html', {'title': title, 'questions': q, 'question_answers': question_answers_dict})


@csrf_exempt
def vote(request, test_id):
    """
    :return: dostaje odpowiedzi użytkownika i zwraca odpowiedź
    """
    if test_id == 1:
        questions = MyQuestions.all_questions(1)
        questions_answers = dict(request.POST)
        del questions_answers['csrfmiddlewaretoken']
        try:
            if len(questions) == len(request.POST) - 1:
                odp = MyQuestions.result(questions_answers)
                return render(request, 'home/results.html', {'title': odp[1], 'kompletne': 'tak'})
            else:
                return render(request, 'home/results.html', {'odp': "Uzupełnij wszystkie pytania. Wróć do testu.", 'kompletne': 'nie'})
        except KeyError:
            return render(request, 'home/results.html', {'odp': "Upss! Coś poszło nie tak. Sprójbuj jeszcze raz!.", 'kompletne': 'nie'})
    elif test_id == 2:
        title = request.POST["title"]
        questions = MyQuestions.all_questions(2)
        questions_answers = dict(request.POST)
        del questions_answers['csrfmiddlewaretoken']
        del questions_answers['title']
        try:
            if len(questions) == len(request.POST) - 2:
                odp = MyQuestions.result_job(questions_answers, title)
                result = Results.objects.get(title=title)
                jobs = [i.job.name for i in result.resultsjobs_set.all()]
                return render(request, 'home/result_job.html', {'odp': odp, 'title': title, 'result':result, 'jobs': jobs, 'kompletne': 'tak'})
            else:
                return render(request, 'home/result_job.html', {'odp': "Uzupełnij wszystkie pytania. Wróć do testu.", 'kompletne': 'nie'})
        except KeyError:
            return render(request, 'home/result_job.html', {'odp': "Wysłałeś pustą odpowiedź. Sprójbuj jeszcze raz!.", 'kompletne': 'nie'})
