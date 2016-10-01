# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0004_nonprofit_partners'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attorney_List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Attorneys', models.CharField(max_length=120, blank=True)),
                ('Status', models.CharField(max_length=50, blank=True)),
                ('Cases', models.CharField(max_length=120, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Opportunity_Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Attorneys', models.CharField(max_length=120, blank=True)),
                ('Cases', models.CharField(max_length=120, blank=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Nonprofit_Partners',
            new_name='Nonprofit_Partner',
        ),
    ]
