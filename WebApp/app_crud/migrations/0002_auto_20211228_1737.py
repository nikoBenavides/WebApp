# Generated by Django 3.2.8 on 2021-12-28 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='person',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='urgency',
        ),
    ]
