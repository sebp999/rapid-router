# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.db import models, migrations
from game.level_management import set_blocks_inner, set_decor_inner



class Migration(migrations.Migration):

    dependencies = [("game", "0047_level_70_is_unsolveable")]

    operations = [
        migrations.AddField(
            model_name="episode",
            name="r_cows",
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="level",
            name="cows",
            field=models.TextField(default="[]", max_length=10000),
            preserve_default=True,
        ),
    ]
