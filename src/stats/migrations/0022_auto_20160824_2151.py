# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0021_auto_20160824_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attorney_list',
            name='Last_Visited',
            field=models.DateTimeField(default=[b'2016-08-24 05:48']),
        ),
    ]
