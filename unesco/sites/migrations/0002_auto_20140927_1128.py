# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=120, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='site',
            name='state',
        ),
        migrations.AddField(
            model_name='site',
            name='http_url',
            field=models.URLField(default='', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='site',
            name='image_url',
            field=models.URLField(default='', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='site',
            name='justification',
            field=models.TextField(max_length=4000, default='', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='site',
            name='region',
            field=models.ForeignKey(null=True, to='sites.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='site',
            name='short_description',
            field=models.TextField(max_length=4000, default='', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='site',
            name='states',
            field=models.ManyToManyField(null=True, to='sites.State'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='state',
            name='iso_code',
            field=models.CharField(max_length=120, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='site',
            name='inscribed_date',
            field=models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='inscribed_date'),
        ),
        migrations.AlterField(
            model_name='site',
            name='latitude',
            field=models.FloatField(null=True, blank=True, verbose_name='latitude'),
        ),
        migrations.AlterField(
            model_name='site',
            name='longitude',
            field=models.FloatField(null=True, blank=True, verbose_name='longitude'),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=120, default=''),
        ),
    ]
