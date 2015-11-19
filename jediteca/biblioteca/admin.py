from django.contrib import admin
from .models import Livro,Autor


class LivroAdmin(admin.ModelAdmin):

    list_display = ('titulo', 'edicao','formato', 'ativo')
    search_fields = ['titulo']

admin.site.register(Livro,LivroAdmin)

admin.site.register(Autor)

# Register your models here.
