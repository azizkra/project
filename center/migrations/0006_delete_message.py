# Generated by Django 4.1.1 on 2022-09-08 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0005_rename_comments_message_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
