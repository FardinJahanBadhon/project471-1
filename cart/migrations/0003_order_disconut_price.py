# Generated by Django 4.2.10 on 2024-04-03 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_order_is_coupon_alter_order_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='disconut_price',
            field=models.FloatField(default=0.0),
        ),
    ]
