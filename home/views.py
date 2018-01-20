from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

def IndexView(request):
    return render_to_response('home/index.html')

def TestView(request):
    return render_to_response('home/test.html')

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
