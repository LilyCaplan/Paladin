# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0019_auto_20160824_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attorney_list',
            name='Last_Visited',
            field=models.DateTimeField(verbose_name=[b'%m/%d/%Y %H:%M:%S.%f']),
        ),
    ]
