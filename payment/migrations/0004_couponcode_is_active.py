# Generated by Django 4.2.10 on 2024-04-03 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_couponcode_discount_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='couponcode',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
