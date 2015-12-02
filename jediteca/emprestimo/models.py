from django.db import models
from core.models import *

class Reserva(models.Model):
    data = models.DateTimeField(auto_now = True)
    ativo = models.BooleanField(default=True)
    livro = models.ForeignKey(Livro)
    leitor = models.ForeignKey('auth.User')

    def __str__(self):
        return self.livro

class Emprestimo(models.Model):
    data_emprestimo = models.DateTimeField(auto_now=True)
    data_devolucao = models.DateTimeField()
    leitor = models.ForeignKey('auth.User')
    livro = models.ForeignKey(Livro)

    def __str__(self):
        return data_emprestimo
