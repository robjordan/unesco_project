# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whsites', '0002_auto_20150102_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='site',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='visitor',
        ),
        migrations.DeleteModel(
            name='Visit',
        ),
    ]
