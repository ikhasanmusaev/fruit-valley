# Generated by Django 3.1.3 on 2020-12-23 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20201223_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description_fr',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_fr',
        ),
    ]
