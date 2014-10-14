# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('favourite_city', models.CharField(default='', max_length=120)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
