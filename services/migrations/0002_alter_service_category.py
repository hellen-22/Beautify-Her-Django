# Generated by Django 4.1.7 on 2023-05-28 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="service",
                to="services.servicecategory",
            ),
        ),
    ]
