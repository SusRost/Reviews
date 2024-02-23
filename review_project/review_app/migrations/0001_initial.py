# Generated by Django 5.0.2 on 2024-02-22 15:13

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Review",
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
                ("content", models.TextField()),
                ("rating", models.FloatField()),
                ("sentiment", models.CharField(max_length=3)),
            ],
        ),
    ]