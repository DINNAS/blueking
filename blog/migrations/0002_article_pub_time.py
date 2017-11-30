# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 29, 10, 18, 8, 408553, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
