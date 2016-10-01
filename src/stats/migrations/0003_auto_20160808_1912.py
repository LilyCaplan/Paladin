# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_auto_20160808_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='Attorneys',
            field=models.CharField(max_length=120, blank=True),
        ),
        migrations.AlterField(
            model_name='stats',
            name='Hours',
            field=models.SmallIntegerField(),
        ),
    ]
