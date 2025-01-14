from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 1
    feature1.name = 'Fast'
    feature1.description = 'Fast service for you'
    feature1.is_true = True

    feature2 = Feature()
    feature2.id = 2
    feature2.name = 'Responsive'
    feature2.description = 'Responsive design for you'
    feature2.is_true = False

    context = {
        'title': 'Home',
        'name': 'John Doe',
        'age': 30,
        'features': [feature1 , feature2]
    }
    return render(request, 'index.html', context)

def counter(request):
    words = request.POST.get('words')
    wordCount = len(words.split())
    context = {
        'title': 'Counter',
        'words': words,
        'word_count': wordCount
    }
    return render(request, 'counter.html', context)