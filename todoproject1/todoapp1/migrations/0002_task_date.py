# Generated by Django 4.1.4 on 2023-01-30 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-04-11'),
            preserve_default=False,
        ),
    ]
