# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome_completo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('avaliacao', models.IntegerField()),
                ('comentario', models.CharField(max_length=250)),
                ('data_hora', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('data_emprestimo', models.DateTimeField(auto_now=True)),
                ('data_devolucao', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Leitor',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('nome_completo', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('titulo', models.CharField(max_length=200)),
                ('edicao', models.PositiveIntegerField()),
                ('ano', models.PositiveIntegerField()),
                ('quantidade', models.PositiveIntegerField()),
                ('sinopse', models.TextField(max_length=500)),
                ('formato', models.CharField(default='FI', max_length=2, choices=[('FI', 'FÍSICO'), ('DI', 'DIGITAL')])),
                ('ativo', models.BooleanField(default=True)),
                ('autores', models.ManyToManyField(to='biblioteca.Autor')),
                ('comentarios', models.ForeignKey(to='biblioteca.Comentario', blank=True)),
                ('editora', models.ForeignKey(to='biblioteca.Editora', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('data', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('leitor', models.ForeignKey(to='biblioteca.Leitor')),
                ('livro', models.ForeignKey(to='biblioteca.Livro')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('texto', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='livro',
            name='tags',
            field=models.ManyToManyField(to='biblioteca.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='leitor',
            name='tags',
            field=models.ForeignKey(to='biblioteca.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='leitor',
            field=models.ForeignKey(to='biblioteca.Leitor'),
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='livro',
            field=models.ForeignKey(to='biblioteca.Livro'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='leitor',
            field=models.ForeignKey(to='biblioteca.Leitor'),
        ),
    ]
