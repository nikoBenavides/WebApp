# Generated by Django 3.2.8 on 2021-12-29 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0008_auto_20211229_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='idCode',
        ),
        migrations.RemoveField(
            model_name='person',
            name='phone',
        ),
    ]
