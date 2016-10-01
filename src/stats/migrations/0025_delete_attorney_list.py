# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0024_remove_attorney_list_total_hours'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attorney_List',
        ),
    ]
