# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_emprestimo', models.DateTimeField(auto_now=True)),
                ('data_devolucao', models.DateTimeField()),
                ('leitor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('livro', models.ForeignKey(to='core.Livro')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('leitor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('livro', models.ForeignKey(to='core.Livro')),
            ],
        ),
    ]
