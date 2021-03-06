# Generated by Django 3.1 on 2020-08-28 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline_date',
            field=models.DateField(default=None, verbose_name='date of deadline'),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline_time',
            field=models.TimeField(default=None, verbose_name='time of deadline'),
        ),
    ]
