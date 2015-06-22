# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Article.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('key', models.BooleanField(default=True)),
                ('body', models.TextField()),
                ('tag', models.CharField(help_text=b'Max. Characters = 30', max_length=30, null=True, blank=True)),
                ('author', models.CharField(default=b'himanshu', max_length=50)),
                ('likes', models.IntegerField(default=0)),
                ('doc', models.FileField(upload_to=Article.models.get_upload_file_name, null=True, verbose_name=b'Attachment', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment', models.TextField()),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('parent_article_id', models.CharField(default=b'', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=25)),
                ('user_password', models.CharField(max_length=25)),
                ('posts', models.IntegerField(default=10)),
                ('user_email', models.CharField(max_length=30)),
                ('user_college', models.CharField(max_length=50)),
                ('photo', models.FileField(default=b'himanshu.jpeg', upload_to=Article.models.get_upload_file_name)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
