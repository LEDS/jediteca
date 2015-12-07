from django.contrib import admin

from core.models import *


class LivroAdmin(admin.ModelAdmin):

    list_display = ('nome', 'edicao','formato', 'ativo')
    search_fields = ['nome']

admin.site.register(Livro,LivroAdmin)

admin.site.register(Autor)

admin.site.register(Editora)

admin.site.register(Comentario)

admin.site.register(Tag)

admin.site.register(Pessoa)

admin.site.register(Link)
