# Generated by Django 4.1.1 on 2022-09-09 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0014_founders_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='founders',
            name='slug',
        ),
    ]
