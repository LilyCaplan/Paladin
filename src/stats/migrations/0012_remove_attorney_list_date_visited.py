# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0011_auto_20160822_0202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attorney_list',
            name='Date_Visited',
        ),
    ]
