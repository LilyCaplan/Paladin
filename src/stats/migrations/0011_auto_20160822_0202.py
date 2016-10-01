# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0010_auto_20160822_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attorney_list',
            name='Date_Visited',
            field=models.DateTimeField(),
        ),
    ]
