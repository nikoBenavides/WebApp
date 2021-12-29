# Generated by Django 3.2.8 on 2021-12-28 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0002_auto_20211228_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_crud.person'),
        ),
        migrations.AddField(
            model_name='activity',
            name='urgency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_crud.urgency'),
        ),
    ]
