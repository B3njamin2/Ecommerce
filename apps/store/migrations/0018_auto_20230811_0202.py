# Generated by Django 3.1 on 2023-08-11 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='last_visit',
        ),
        migrations.RemoveField(
            model_name='product',
            name='num_visits',
        ),
    ]
