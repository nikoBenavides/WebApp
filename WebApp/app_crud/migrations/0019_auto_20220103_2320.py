# Generated by Django 3.2.8 on 2022-01-04 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0018_auto_20220103_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_date_created',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_date_end',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
