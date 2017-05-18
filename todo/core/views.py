from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from core.forms import TodoForm
from core.models import Todo

# Create your views here.


def network():
    raise ValueError


def index(request):
    network()
    todos = Todo.objects.all()
    return render(request, 'index.html', context={'todos': todos})


def create(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseBadRequest()
