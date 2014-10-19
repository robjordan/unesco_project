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
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20, default='')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=120, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=120, default='')),
                ('iso_code', models.CharField(max_length=120, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('comments', models.TextField(max_length=4000, default='', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WHSite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(default='', unique=True)),
                ('id_number', models.PositiveSmallIntegerField(verbose_name='ID number', null=True)),
                ('short_description', models.TextField(max_length=4000, default='', blank=True)),
                ('justification', models.TextField(max_length=4000, default='', blank=True)),
                ('http_url', models.URLField(default='', blank=True, verbose_name='URL')),
                ('image_url', models.URLField(default='', blank=True, verbose_name='Image URL')),
                ('inscribed_date', models.PositiveSmallIntegerField(verbose_name='inscribed date', blank=True, null=True)),
                ('latitude', models.FloatField(verbose_name='latitude', blank=True, null=True)),
                ('longitude', models.FloatField(verbose_name='longitude', blank=True, null=True)),
                ('category', models.ForeignKey(null=True, to='whsites.Category')),
                ('region', models.ForeignKey(null=True, to='whsites.Region')),
                ('states', models.ManyToManyField(null=True, to='whsites.State')),
            ],
            options={
                'verbose_name': 'UNESCO Site',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='visit',
            name='site',
            field=models.ForeignKey(to='whsites.WHSite'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='visit',
            name='visitor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
