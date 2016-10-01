# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0008_auto_20160818_0445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nonprofit_partner',
            name='Image',
        ),
        migrations.AlterField(
            model_name='nonprofit_partner',
            name='Nonprofit',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
