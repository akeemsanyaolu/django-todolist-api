# Generated by Django 4.1.8 on 2023-08-02 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created',
        ),
    ]
