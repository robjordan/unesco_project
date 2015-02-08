# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whsites', '0002_auto_20150102_1905'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='visits',
            field=models.ManyToManyField(null=True, to='whsites.Visit'),
            preserve_default=True,
        ),
    ]
