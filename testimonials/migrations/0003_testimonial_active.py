# Generated by Django 4.1.5 on 2023-02-19 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_testimonial_create_at_testimonial_update_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
    ]
