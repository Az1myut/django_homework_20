# Generated by Django 4.1.5 on 2023-02-08 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Изображение'),
        ),
    ]
