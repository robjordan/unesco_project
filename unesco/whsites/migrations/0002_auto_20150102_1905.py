# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('whsites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='whsite',
            name='globe_point',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326, geography=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whsite',
            name='map_point',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326, blank=True),
            preserve_default=True,
        ),
    ]
