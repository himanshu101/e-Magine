# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0003_article_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='num_comm',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 7, 13, 51, 37, 562308, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
    ]
