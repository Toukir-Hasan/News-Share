# Generated by Django 4.1.3 on 2022-11-24 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_user_readlater_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='readlater',
            old_name='user_name',
            new_name='name',
        ),
    ]
