from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Tag (models.Model):

    texto = models.CharField(max_length=20)

    def __str__(self):
        return self.texto

class Comentario(models.Model):

    avaliacao = models.IntegerField()
    comentario = models.CharField(max_length=250)
    data_hora = models.DateTimeField(auto_now = True)
    leitor = models.ForeignKey('auth.User')

    def __str__(self):
        return self.comentario

class ItemConhecimento(models.Model):

    tags = models.ManyToManyField(Tag, blank=True,db_index=True)
    comentarios = models.ForeignKey(Comentario, blank = True)
    descricao = models.TextField(max_length=500)
    nome = models.CharField(max_length=100,db_index=True)


    class Meta:
        abstract = True

class Link (ItemConhecimento):

    url = models.URLField()

    def __str__(self):
        return self.nome

class Pessoa (ItemConhecimento):

    email = models.EmailField()
    site = models.URLField()

    def __str__(self):
        return self.nome

class Autor (models.Model):
    nome_completo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_completo


class Editora(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Livro (ItemConhecimento):

    FISICO = 'FI'
    DIGITAL = 'DI'

    TIPO_LIVRO = (
        (FISICO, 'FÍSICO'),
        (DIGITAL, 'DIGITAL'),
    )

    edicao = models.PositiveIntegerField(db_index=True)
    ano = models.PositiveIntegerField(db_index=True)
    quantidade = models.PositiveIntegerField()
    formato = models.CharField(max_length=2,
                                      choices=TIPO_LIVRO,
                                      default=FISICO)
    ativo = models.BooleanField(default=True)
    autores = models.ManyToManyField(Autor,db_index=True)
    editora = models.ForeignKey(Editora,blank = True,db_index=True)
    image = models.ImageField()

    def __str__(self):
        return self.titulo

    @staticmethod
    def find_all(offset,limit,order_by):
        return Livro.objects.order_by(order_by).all()[offset: limit]
