# Generated by Django 4.2.1 on 2023-06-04 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0003_alter_order_customer_alter_orderitem_order_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="payment_status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Complete", "Complete"),
                    ("Failed", "Failed"),
                ],
                default="Pending",
                max_length=100,
            ),
        ),
    ]
