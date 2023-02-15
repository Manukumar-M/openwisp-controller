# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-03 15:47
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('pki', '0001_initial')]

    operations = [
        migrations.AddField(
            model_name='ca',
            name='organization_name',
            field=models.CharField(
                blank=True, max_length=64, verbose_name='organization'
            ),
        ),
        migrations.AddField(
            model_name='cert',
            name='organization_name',
            field=models.CharField(
                blank=True, max_length=64, verbose_name='organization'
            ),
        ),
    ]
