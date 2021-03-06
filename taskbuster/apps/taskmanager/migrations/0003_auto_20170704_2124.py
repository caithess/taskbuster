# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 04:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0002_auto_20170704_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='taskmanager.Profile', verbose_name='user')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ('user', 'name'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('user', 'name')]),
        ),
    ]
