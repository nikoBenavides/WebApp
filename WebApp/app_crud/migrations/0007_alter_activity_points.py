# Generated by Django 3.2.8 on 2021-12-29 05:51

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0006_alter_activity_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='points',
            field=models.FloatField(null=True, verbose_name=builtins.sum),
        ),
    ]
