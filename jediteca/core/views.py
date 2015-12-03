from django.shortcuts import render
from .models import Livro
# Create your views here.

def tela_login(request):
    return render(request,'jediteca/tela_login.html', {'livros':Livro.objects.all()})

def livros_list(request):
    return render(request, 'jediteca/livros_list.html', {'livros':Livro.objects.all()})
