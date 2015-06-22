# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0006_auto_20150407_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 8, 8, 44, 7, 57548, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
    ]
