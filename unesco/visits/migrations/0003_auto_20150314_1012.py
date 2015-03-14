# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0002_auto_20150314_0915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='approx_date',
            new_name='date',
        ),
    ]
