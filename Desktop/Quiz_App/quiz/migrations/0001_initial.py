# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-05 11:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        # migrations.CreateModel(
        #     name='Choice',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('choice', models.CharField(max_length=200)),
        #         ('is_right_answer', models.BooleanField(default=False)),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='Question',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('question', models.CharField(max_length=200)),
        #         ('question_seq_number', models.IntegerField()),
        #     ],
        # ),
        # migrations.AddField(
        #     model_name='choice',
        #     name='question',
        #     field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question'),
        # ),
    ]
