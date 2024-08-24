from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание продукта",
    )
    image = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото товара",
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        null=True,
        blank=True,
        related_name='products',
    )
    price = models.FloatField(
        verbose_name="Цена продукта",
        help_text="Введите цену продукта",

    )
    created_at = models.DateField(
        verbose_name="Дата создания (записи в БД)",
        help_text="Введите дату создания продукта (записи  в БД) ",
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения (записи в БД)",
        help_text="Введите дату последнего изменения продукта (записи  в БД)",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name", "price", "created_at", "updated_at"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание категории",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name
