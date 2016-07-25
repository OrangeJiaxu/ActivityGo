# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_user_headimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=50)),
                ('adate', models.CharField(max_length=20)),
                ('alocation', models.CharField(max_length=50)),
                ('adescription', models.CharField(max_length=200)),
                ('aorganiser', models.CharField(max_length=50)),
                ('aparticipantnum', models.IntegerField(default=0)),
                ('astatus', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='headImg',
            field=models.FileField(default='activity/static/01.jpg', upload_to='activity/static/images/'),
        ),
        migrations.AddField(
            model_name='activities',
            name='aparticipants',
            field=models.ManyToManyField(to='activity.User'),
        ),
    ]
