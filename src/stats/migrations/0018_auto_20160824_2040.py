# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0017_auto_20160824_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attorney_list',
            name='Last_Visited',
            field=models.DateTimeField(verbose_name=[b'%Y-%m-%d %H:%M:%S']),
        ),
    ]
