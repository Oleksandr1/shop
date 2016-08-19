# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sort',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Sort', max_length=256)),
                ('description', models.TextField(verbose_name='Description')),
                ('photo', models.ImageField(upload_to='', verbose_name='Photo', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Sorts',
                'verbose_name': 'Sort',
            },
        ),
    ]
