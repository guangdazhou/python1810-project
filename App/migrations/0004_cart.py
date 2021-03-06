# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-04 12:53
from __future__ import unicode_literals

import App.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_showgoods'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.FloatField(verbose_name=App.models.User)),
                ('number', models.IntegerField()),
                ('isselect', models.BooleanField(default=True)),
                ('showgoods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Showgoods')),
            ],
            options={
                'db_table': 'app_cart',
            },
        ),
    ]
