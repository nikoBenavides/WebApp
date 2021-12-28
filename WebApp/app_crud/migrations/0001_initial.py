# Generated by Django 3.2.8 on 2021-12-28 06:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Urgency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urgency', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('idCode', models.CharField(max_length=5)),
                ('phone', models.CharField(max_length=10)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_crud.position')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=500, null=True)),
                ('activity_description', models.CharField(max_length=1000, null=True)),
                ('activity_date_created', models.DateField(default=datetime.date.today, null=True)),
                ('activity_date_end', models.DateField(default=datetime.date.today, null=True)),
                ('hours', models.CharField(max_length=2, null=True)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_crud.person')),
                ('urgency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_crud.urgency')),
            ],
        ),
    ]
