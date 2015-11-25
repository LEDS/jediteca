# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_auto_20151125_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='ano',
            field=models.PositiveIntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='edicao',
            field=models.PositiveIntegerField(db_index=True),
        ),
    ]
