from django.contrib import admin

from .models import *


class LivroAdmin(admin.ModelAdmin):

    list_display = ('titulo', 'edicao','formato', 'ativo')
    search_fields = ['titulo']

admin.site.register(Livro,LivroAdmin)

admin.site.register(Autor)

admin.site.register(Editora)

admin.site.register(Comentario)

admin.site.register(Tag)
