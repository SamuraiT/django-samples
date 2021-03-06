from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
# Create your views here.
from .models import Question

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]

    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context) 

def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/detail.html', {'question': question}) 
