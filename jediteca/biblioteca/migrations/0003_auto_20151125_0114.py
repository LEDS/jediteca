# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_livro_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='autores',
            field=models.ManyToManyField(to='biblioteca.Autor', db_index=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='tags',
            field=models.ManyToManyField(blank=True, to='biblioteca.Tag', db_index=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='titulo',
            field=models.CharField(max_length=200, db_index=True),
        ),
    ]
