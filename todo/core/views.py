import random

from django.shortcuts import render, redirect

# Create your views here.
from core.forms import TestForm

TASKS = {
    '1': {
        'title': 'test1',
        'text': 'text1',
    },
    '2': {
        'title': 'test2',
        'text': 'text2',
    },
    '3': {
        'title': 'test3',
        'text': 'text3',
    }
}


def index(request):
    return render(request, 'index.html', context={'tasks': TASKS.items()})


def details(request, task_id):
    print(task_id)
    return render(request, 'index.html')


def form_view(request):
    if request.method == 'GET':
        form = TestForm()
        return render(request, 'form.html', context={'form': form})
    else:
        form = TestForm(request.POST)
        if form.is_valid():
            TASKS[random.randint(0, 100000)] = form.cleaned_data
            return redirect('index')
        else:
            return render(request, 'form.html', context={'form': form})
