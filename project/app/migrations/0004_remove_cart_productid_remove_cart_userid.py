# Generated by Django 4.2.6 on 2023-11-03 06:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_cart"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="productid",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="userid",
        ),
    ]