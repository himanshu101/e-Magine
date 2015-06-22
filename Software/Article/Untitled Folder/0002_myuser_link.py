# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='link',
            field=models.CharField(default=b'', max_length=20),
            preserve_default=True,
        ),
    ]
