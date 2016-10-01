# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0003_auto_20160808_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nonprofit_Partners',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Image', models.ImageField(upload_to=b'')),
                ('Nonprofit', models.CharField(max_length=100)),
            ],
        ),
    ]
