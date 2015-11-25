from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Tag (models.Model):

    texto = models.CharField(max_length=20)

    def __str__(self):
        return self.texto

class Leitor (AbstractBaseUser):

    email = models.EmailField()
    nome_completo = models.CharField(max_length=100)
    tags = models.ForeignKey(Tag,blank=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username

class Autor (models.Model):
    nome_completo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_completo


class Editora(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Comentario(models.Model):

    avaliacao = models.IntegerField()
    comentario = models.CharField(max_length=250)
    data_hora = models.DateTimeField(auto_now = True)
    leitor = models.ForeignKey(Leitor)

    def __str__(self):
        return self.comentario

class Livro (models.Model):

    FISICO = 'FI'
    DIGITAL = 'DI'

    TIPO_LIVRO = (
        (FISICO, 'FÍSICO'),
        (DIGITAL, 'DIGITAL'),
    )

    titulo = models.CharField(max_length=200,db_index=True)
    edicao = models.PositiveIntegerField(db_index=True)
    ano = models.PositiveIntegerField(db_index=True)
    quantidade = models.PositiveIntegerField()
    sinopse = models.TextField(max_length=500)
    formato = models.CharField(max_length=2,
                                      choices=TIPO_LIVRO,
                                      default=FISICO)
    ativo = models.BooleanField(default=True)
    autores = models.ManyToManyField(Autor,db_index=True)
    editora = models.ForeignKey(Editora,blank = True,db_index=True)
    comentarios = models.ForeignKey(Comentario, blank = True)
    tags = models.ManyToManyField(Tag, blank=True,db_index=True)
    image = models.ImageField()

    def __str__(self):
        return self.titulo


class Reserva(models.Model):
    data = models.DateTimeField(auto_now = True)
    ativo = models.BooleanField(default=True)
    livro = models.ForeignKey(Livro)
    leitor = models.ForeignKey(Leitor)

    def __str__(self):
        return self.livro

class Emprestimo(models.Model):
    data_emprestimo = models.DateTimeField(auto_now=True)
    data_devolucao = models.DateTimeField()
    leitor = models.ForeignKey(Leitor)
    livro = models.ForeignKey(Livro)

    def __str__(self):
        return data_emprestimo
