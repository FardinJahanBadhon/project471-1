# Generated by Django 5.0.2 on 2024-04-16 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0016_alter_product_skin_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='skin_type',
        ),
    ]
