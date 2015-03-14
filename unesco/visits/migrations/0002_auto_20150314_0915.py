# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_date_extensions.fields
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='date',
        ),
        migrations.AddField(
            model_name='visit',
            name='approx_date',
            field=django_date_extensions.fields.ApproximateDateField(default=datetime.datetime(2015, 3, 14, 9, 15, 12, 589957, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
    ]
