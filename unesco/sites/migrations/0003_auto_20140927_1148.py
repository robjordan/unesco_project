# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_auto_20140927_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(default='', max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='site',
            name='category',
            field=models.ForeignKey(to='sites.Category', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='site',
            name='id_number',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='ID number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='site',
            name='http_url',
            field=models.URLField(default='', verbose_name='URL', blank=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='image_url',
            field=models.URLField(default='', verbose_name='Image URL', blank=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='inscribed_date',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='inscribed date', blank=True),
        ),
    ]
