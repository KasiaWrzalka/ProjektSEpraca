from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render_to_response('home/index.html')

def test(request):
    return render_to_response('home/test.html')

@csrf_exempt
def vote(request, test_id):
    print('post')
    print(request, test_id)
    return render_to_response('home/index.html')
    # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))