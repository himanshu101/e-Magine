# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0003_auto_20150325_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='user_permission',
            field=models.IntegerField(default=2),
            preserve_default=True,
        ),
    ]
