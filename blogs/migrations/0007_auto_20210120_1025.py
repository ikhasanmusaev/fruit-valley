# Generated by Django 3.1.3 on 2021-01-20 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20201228_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='body_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='body_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='body_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='content_image',
            field=models.ImageField(upload_to='articles/'),
        ),
    ]
