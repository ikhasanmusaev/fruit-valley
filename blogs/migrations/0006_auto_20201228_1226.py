# Generated by Django 3.1.3 on 2020-12-28 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20201223_1420'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-id']},
        ),
    ]
