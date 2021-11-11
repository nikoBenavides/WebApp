# Generated by Django 3.2.8 on 2021-11-10 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0002_rename_persona_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='ACtivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('urgency', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='idCode',
            field=models.CharField(max_length=5),
        ),
    ]
