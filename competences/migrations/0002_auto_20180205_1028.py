# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-05 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competences', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='user',
        ),
        migrations.AlterField(
            model_name='detail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profil', verbose_name='utilisateur concerné'),
        ),
        migrations.DeleteModel(
            name='Profil',
        ),
    ]