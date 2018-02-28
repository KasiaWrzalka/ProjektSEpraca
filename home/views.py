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
    print(request)
    print('********************')
    print(request.POST)
    try:
        if request.POST[('choice')] == 'tak':
            odp = "Jesteś introwertykiem!"
        elif request.POST[('choice')] == "nie":
            odp = "Jesteś extrawertykiem!"
        else:
            odp = " Wróć do testu i uzupełnij pytanie"
        return render(request, 'home/results.html', {'odp': odp})
    except (KeyError):
        return render(request, 'home/results.html', {'odp': "Wysłałeś pustą odpowiedź. Sprójbuj jeszcze raz!."})

