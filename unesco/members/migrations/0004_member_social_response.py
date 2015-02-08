# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_remove_member_visits'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='social_response',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
