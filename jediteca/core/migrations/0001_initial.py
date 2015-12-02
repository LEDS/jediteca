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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_completo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avaliacao', models.IntegerField()),
                ('comentario', models.CharField(max_length=250)),
                ('data_hora', models.DateTimeField(auto_now=True)),
                ('leitor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.TextField(max_length=500)),
                ('nome', models.CharField(db_index=True, max_length=100)),
                ('url', models.URLField()),
                ('comentarios', models.ForeignKey(blank=True, to='core.Comentario')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.TextField(max_length=500)),
                ('nome', models.CharField(db_index=True, max_length=100)),
                ('edicao', models.PositiveIntegerField(db_index=True)),
                ('ano', models.PositiveIntegerField(db_index=True)),
                ('quantidade', models.PositiveIntegerField()),
                ('formato', models.CharField(choices=[('FI', 'FÍSICO'), ('DI', 'DIGITAL')], default='FI', max_length=2)),
                ('ativo', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='')),
                ('autores', models.ManyToManyField(db_index=True, to='core.Autor')),
                ('comentarios', models.ForeignKey(blank=True, to='core.Comentario')),
                ('editora', models.ForeignKey(blank=True, to='core.Editora')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.TextField(max_length=500)),
                ('nome', models.CharField(db_index=True, max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('site', models.URLField()),
                ('comentarios', models.ForeignKey(blank=True, to='core.Comentario')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='pessoa',
            name='tags',
            field=models.ManyToManyField(db_index=True, blank=True, to='core.Tag'),
        ),
        migrations.AddField(
            model_name='livro',
            name='tags',
            field=models.ManyToManyField(db_index=True, blank=True, to='core.Tag'),
        ),
        migrations.AddField(
            model_name='link',
            name='tags',
            field=models.ManyToManyField(db_index=True, blank=True, to='core.Tag'),
        ),
    ]
