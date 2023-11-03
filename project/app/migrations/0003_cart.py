# Generated by Django 4.2.6 on 2023-11-03 05:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("userid", models.IntegerField()),
                ("productid", models.IntegerField()),
                ("title", models.CharField(max_length=100)),
                ("price", models.IntegerField()),
                ("brand", models.CharField(max_length=20)),
            ],
            options={
                "db_table": "cart_table",
            },
        ),
    ]