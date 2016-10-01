# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0009_auto_20160818_0524'),
    ]

    operations = [
        migrations.AddField(
            model_name='attorney_list',
            name='Date_Visited',
            field=models.DateTimeField(default=b''),
        ),
        migrations.AddField(
            model_name='attorney_list',
            name='Total_Hours',
            field=models.SmallIntegerField(default=b''),
        ),
    ]
