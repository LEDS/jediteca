# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nome_completo', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='livro',
            name='autores',
            field=models.ManyToManyField(to='biblioteca.Autor'),
        ),
    ]
