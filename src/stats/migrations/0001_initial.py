# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Active_Attorneys', models.IntegerField()),
                ('Total_Hours', models.IntegerField()),
                ('Average_Hours', models.IntegerField()),
                ('Completed_Projects', models.IntegerField()),
            ],
        ),
    ]
