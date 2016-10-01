# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0012_remove_attorney_list_date_visited'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attorney_list',
            name='Total_Hours',
        ),
    ]
