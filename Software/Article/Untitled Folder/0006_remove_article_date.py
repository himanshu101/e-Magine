# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0005_article_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='date',
        ),
    ]
