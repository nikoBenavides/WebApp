# Generated by Django 3.2.8 on 2021-12-31 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0009_auto_20211229_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='points_sts',
            field=models.CharField(default='1', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='urgency',
            name='points_urg',
            field=models.CharField(default='1', max_length=50),
            preserve_default=False,
        ),
    ]
