# Generated by Django 3.1.3 on 2021-03-18 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('name_ru', models.CharField(max_length=127, null=True)),
                ('name_en', models.CharField(max_length=127, null=True)),
                ('name_uz', models.CharField(max_length=127, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_uz', models.TextField(blank=True, null=True)),
                ('slug', models.CharField(max_length=31, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='category/')),
                ('status', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('name_ru', models.CharField(max_length=127, null=True)),
                ('name_en', models.CharField(max_length=127, null=True)),
                ('name_uz', models.CharField(max_length=127, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_uz', models.TextField(blank=True, null=True)),
                ('price_for_weight', models.CharField(default=0, max_length=11)),
                ('price_for_qty', models.CharField(default=0, max_length=11)),
                ('status', models.IntegerField(choices=[(1, 'In Stock'), (0, 'Out Of Stock')], default=1)),
                ('sale', models.IntegerField(default=0, help_text='Sale on percent')),
                ('min_weight', models.IntegerField(blank=True, null=True)),
                ('min_qty', models.IntegerField(blank=True, null=True)),
                ('sku', models.CharField(max_length=63)),
                ('date_of_created', models.DateTimeField(auto_now_add=True)),
                ('number_of_pieces', models.IntegerField(blank=True, null=True)),
                ('ingredients', models.TextField(blank=True, null=True)),
                ('ingredients_ru', models.TextField(blank=True, null=True)),
                ('ingredients_en', models.TextField(blank=True, null=True)),
                ('ingredients_uz', models.TextField(blank=True, null=True)),
                ('recipes', models.TextField(blank=True, null=True)),
                ('recipes_ru', models.TextField(blank=True, null=True)),
                ('recipes_en', models.TextField(blank=True, null=True)),
                ('recipes_uz', models.TextField(blank=True, null=True)),
                ('product_from', models.CharField(blank=True, max_length=127, null=True)),
                ('product_from_ru', models.CharField(blank=True, max_length=127, null=True)),
                ('product_from_en', models.CharField(blank=True, max_length=127, null=True)),
                ('product_from_uz', models.CharField(blank=True, max_length=127, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to=products.models.product_image_path)),
                ('type', models.IntegerField(choices=[(1, 'Productmainimage'), (2, 'Categorymainimage'), (3, 'Nutritionfacts')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('rating', models.IntegerField(blank=True, choices=[(1, 'One'), (2, 'Two'), (3, 'Third'), (4, 'Four'), (5, 'Five')], null=True)),
                ('status', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productimage'),
        ),
        migrations.CreateModel(
            name='FavouriteProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
