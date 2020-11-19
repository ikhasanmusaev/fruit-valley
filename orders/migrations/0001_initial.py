# Generated by Django 3.1.3 on 2020-11-19 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('method_key', models.CharField(max_length=128, unique=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingMethods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('mini_description', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('period', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('min_order_cost', models.IntegerField(default=0)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveSmallIntegerField()),
                ('qty', models.PositiveSmallIntegerField(default=1)),
                ('type_of_selling', models.CharField(blank=True, choices=[('weight', 'Weight'), ('qty', 'Qty')], max_length=15)),
                ('total', models.PositiveSmallIntegerField()),
                ('date_of_creat', models.DateTimeField(auto_now_add=True)),
                ('date_of_delivery', models.DateTimeField(blank=True, null=True)),
                ('date_of_cancel', models.DateTimeField(blank=True, null=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('method_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.paymentmethods')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_selling', models.CharField(blank=True, choices=[('weight', 'Weight'), ('qty', 'Qty')], max_length=15)),
                ('total', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('date_of_creat', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
