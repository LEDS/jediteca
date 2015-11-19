# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('edicao', models.CharField(max_length=1)),
                ('ano', models.IntegerField()),
                ('quantidade', models.IntegerField()),
                ('sinopse', models.TextField(max_length=500)),
                ('formato', models.CharField(default='FI', max_length=2, choices=[('FI', 'FÍSICO'), ('DI', 'DIGITAL')])),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
