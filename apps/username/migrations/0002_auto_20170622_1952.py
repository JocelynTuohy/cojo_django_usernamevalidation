# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 19:52
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('username', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='username',
            managers=[
                ('usernameManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
