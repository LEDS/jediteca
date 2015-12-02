# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('data_emprestimo', models.DateTimeField(auto_now=True)),
                ('data_devolucao', models.DateTimeField()),
                ('leitor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('livro', models.ForeignKey(to='core.Livro')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('data', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('leitor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('livro', models.ForeignKey(to='core.Livro')),
            ],
        ),
    ]
