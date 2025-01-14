from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    features = Feature.objects.all()
    context = {
        'title': 'Home',
        'name': 'John Doe',
        'age': 30,
        'features': features
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