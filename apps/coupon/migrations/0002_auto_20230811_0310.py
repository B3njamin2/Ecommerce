# Generated by Django 3.1 on 2023-08-11 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='active',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='num_available',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='num_used',
        ),
    ]
