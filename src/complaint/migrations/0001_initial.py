# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120, null=True, blank=True)),
                ('complaint_type', models.CharField(max_length=120, null=True, blank=True)),
                ('complaint_desc', models.CharField(max_length=120, null=True, blank=True)),
                ('address', models.CharField(max_length=120, null=True, blank=True)),
                ('city', models.CharField(max_length=120, null=True, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
