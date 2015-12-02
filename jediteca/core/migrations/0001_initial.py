# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nome_completo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('avaliacao', models.IntegerField()),
                ('comentario', models.CharField(max_length=250)),
                ('data_hora', models.DateTimeField(auto_now=True)),
                ('leitor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item_Conhecimento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('descricao', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('texto', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('item_conhecimento_ptr', models.OneToOneField(to='core.Item_Conhecimento', parent_link=True, primary_key=True, auto_created=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
            bases=('core.item_conhecimento',),
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('item_conhecimento_ptr', models.OneToOneField(to='core.Item_Conhecimento', parent_link=True, primary_key=True, auto_created=True, serialize=False)),
                ('titulo', models.CharField(max_length=200, db_index=True)),
                ('edicao', models.PositiveIntegerField(db_index=True)),
                ('ano', models.PositiveIntegerField(db_index=True)),
                ('quantidade', models.PositiveIntegerField()),
                ('formato', models.CharField(max_length=2, default='FI', choices=[('FI', 'FÍSICO'), ('DI', 'DIGITAL')])),
                ('ativo', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='')),
                ('autores', models.ManyToManyField(to='core.Autor', db_index=True)),
                ('editora', models.ForeignKey(to='core.Editora', blank=True)),
            ],
            bases=('core.item_conhecimento',),
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('item_conhecimento_ptr', models.OneToOneField(to='core.Item_Conhecimento', parent_link=True, primary_key=True, auto_created=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('site', models.URLField()),
            ],
            bases=('core.item_conhecimento',),
        ),
        migrations.AddField(
            model_name='item_conhecimento',
            name='comentarios',
            field=models.ForeignKey(to='core.Comentario', blank=True),
        ),
        migrations.AddField(
            model_name='item_conhecimento',
            name='tags',
            field=models.ManyToManyField(to='core.Tag', db_index=True, blank=True),
        ),
    ]
