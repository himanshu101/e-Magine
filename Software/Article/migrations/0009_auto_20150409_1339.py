# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0008_auto_20150408_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like_articles',
            field=models.CharField(default=b'', max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 9, 8, 9, 26, 287914, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 9, 8, 9, 26, 288486, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
    ]
