# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stats',
            name='Active_Attorneys',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='Average_Hours',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='Total_Hours',
        ),
        migrations.AddField(
            model_name='stats',
            name='Attorneys',
            field=models.CharField(default=None, max_length=120),
        ),
        migrations.AddField(
            model_name='stats',
            name='Hours',
            field=models.SmallIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='stats',
            name='Completed_Projects',
            field=models.SmallIntegerField(),
        ),
    ]
