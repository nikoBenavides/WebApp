# Generated by Django 3.2.8 on 2021-12-29 05:37

import app_crud.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0005_activity_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='points',
            field=models.FloatField(null=True, verbose_name=app_crud.models.SumPoints),
        ),
    ]