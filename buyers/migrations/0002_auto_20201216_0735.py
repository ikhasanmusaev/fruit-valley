# Generated by Django 3.1.3 on 2020-12-16 07:35

import buyers.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', buyers.models.UserManager()),
            ],
        ),
    ]