# Generated by Django 4.1.3 on 2022-11-26 03:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0004_alter_readlater_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readlater',
            name='name',
            field=models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
