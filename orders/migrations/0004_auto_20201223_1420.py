# Generated by Django 3.1.3 on 2020-12-23 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20201223_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentmethods',
            name='name_fr',
        ),
        migrations.RemoveField(
            model_name='shippingmethods',
            name='description_fr',
        ),
        migrations.RemoveField(
            model_name='shippingmethods',
            name='mini_description_fr',
        ),
        migrations.RemoveField(
            model_name='shippingmethods',
            name='name_fr',
        ),
    ]