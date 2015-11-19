from django.db import models

class Autor (models.Model):
    nome_completo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_completo

class Livro (models.Model):

    FISICO = 'FI'
    DIGITAL = 'DI'

    TIPO_LIVRO = (
        (FISICO, 'FÍSICO'),
        (DIGITAL, 'DIGITAL'),
    )

    titulo = models.CharField(max_length=200)
    edicao = models.CharField(max_length=1)
    ano = models.IntegerField()
    quantidade = models.IntegerField()
    sinopse = models.TextField(max_length=500)
    formato = models.CharField(max_length=2,
                                      choices=TIPO_LIVRO,
                                      default=FISICO)
    ativo = models.BooleanField(default=True)
    autores = models.ManyToManyField(Autor)

    def __str__(self):
        return self.titulo
