# Generated by Django 5.1 on 2024-08-28 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                (
                    "name",
                    models.CharField(
                        help_text="Введите наименование категории",
                        max_length=150,
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание категории", verbose_name="Описание"
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                (
                    "name",
                    models.CharField(
                        help_text="Введите наименование продукта",
                        max_length=150,
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание продукта", verbose_name="Описание"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото товара",
                        null=True,
                        upload_to="product/photo",
                        verbose_name="Фото",
                    ),
                ),
                (
                    "price",
                    models.FloatField(
                        help_text="Введите цену продукта", verbose_name="Цена продукта"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания (записи в БД)"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        verbose_name="Дата последнего изменения (записи в БД)",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите категорию продукта",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="catalog.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["category", "name", "price", "created_at", "updated_at"],
            },
        ),
    ]
