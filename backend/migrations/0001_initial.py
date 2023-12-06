# Generated by Django 4.2.7 on 2023-12-05 07:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
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
                ("name", models.CharField(max_length=32)),
                ("description", models.CharField(max_length=1028)),
                (
                    "ratings",
                    models.IntegerField(
                        blank=True,
                        default=1,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
                (
                    "hotels",
                    models.IntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(2000),
                        ],
                    ),
                ),
                (
                    "gardens",
                    models.IntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(200),
                        ],
                    ),
                ),
            ],
            options={
                "db_table": "m_city",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Itinerary",
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
                ("start_day", models.DateField()),
                ("end_day", models.DateField()),
                (
                    "peoples",
                    models.IntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="itinerary_city",
                        to="backend.city",
                    ),
                ),
            ],
            options={
                "db_table": "m_itinerary",
                "ordering": ["id"],
            },
        ),
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
                ("city1", models.CharField(max_length=100)),
                ("user_name", models.CharField(max_length=50)),
                ("rating", models.IntegerField()),
                ("comment", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Planning",
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
                ("day", models.DateField()),
                ("activity", models.TextField()),
                (
                    "itinerary",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="itinerary_city",
                        to="backend.itinerary",
                    ),
                ),
            ],
            options={
                "db_table": "m_planning",
                "ordering": ["day"],
            },
        ),
        migrations.AddIndex(
            model_name="city",
            index=models.Index(fields=["name"], name="city-db-name-idx"),
        ),
        migrations.AlterUniqueTogether(
            name="city",
            unique_together={("name",)},
        ),
        migrations.AddIndex(
            model_name="planning",
            index=models.Index(fields=["day"], name="planning-db-itinerary-idx"),
        ),
        migrations.AddIndex(
            model_name="itinerary",
            index=models.Index(fields=["start_day"], name="itinerary-db-name-idx"),
        ),
    ]
