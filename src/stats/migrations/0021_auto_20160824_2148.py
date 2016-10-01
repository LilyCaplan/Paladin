# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0020_auto_20160824_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attorney_list',
            name='Last_Visited',
            field=models.DateTimeField(verbose_name=[b'2016-08-24 05:48']),
        ),
    ]
