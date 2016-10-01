# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0013_remove_attorney_list_total_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='attorney_list',
            name='Last_Visited',
            field=models.DateTimeField(default=b'%m/%d/%y %H:%M'),
        ),
        migrations.AddField(
            model_name='attorney_list',
            name='Total_Hours',
            field=models.SmallIntegerField(default=b''),
        ),
    ]
