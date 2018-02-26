from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from .models import Questions
from .logic import MyQuestions

def IndexView(request):
    return render_to_response('home/index.html')

def TestView(request):
    q = MyQuestions.all_questions()
    return render(request, 'home/test.html', {'questions': q})

@csrf_exempt
def vote(request, test_id):
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

