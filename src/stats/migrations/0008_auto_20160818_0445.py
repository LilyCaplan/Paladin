# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0007_auto_20160818_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nonprofit_partner',
            name='Image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
