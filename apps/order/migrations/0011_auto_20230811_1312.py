# Generated by Django 3.1 on 2023-08-11 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20230811_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_intent',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipped_date',
        ),
    ]
