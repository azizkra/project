# Generated by Django 4.1.1 on 2022-09-27 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0020_rename_messages_contactus_message'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactUS',
            new_name='Contact',
        ),
    ]
