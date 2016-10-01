# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0005_auto_20160808_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opportunity_request',
            name='Attorneys',
        ),
        migrations.RemoveField(
            model_name='opportunity_request',
            name='Cases',
        ),
        migrations.AddField(
            model_name='opportunity_request',
            name='Attorneys_Who_Request',
            field=models.CharField(default=b'', max_length=120),
        ),
        migrations.AddField(
            model_name='opportunity_request',
            name='Requested_Cases',
            field=models.CharField(default=b'', max_length=120),
        ),
        migrations.AlterField(
            model_name='attorney_list',
            name='Attorneys',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='attorney_list',
            name='Cases',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='attorney_list',
            name='Status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='stats',
            name='Attorneys',
            field=models.CharField(max_length=120),
        ),
    ]
