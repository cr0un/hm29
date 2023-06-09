from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    lat = models.FloatField(verbose_name="Широта")
    lng = models.FloatField(verbose_name="Долгота")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class User(models.Model):
    STATUS = [
        ("member", "Гость"),
        ("moderator", "Модератор"),
        ("admin", "Администратор")
    ]
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    username = models.CharField(max_length=100, verbose_name="Имя пользователя")
    password = models.CharField(max_length=100, verbose_name="Пароль")
    role = models.CharField(max_length=20, verbose_name="Роль", default="member", choices=STATUS)
    age = models.PositiveSmallIntegerField(verbose_name="Возраст")
    locations = models.ManyToManyField(Location, verbose_name="Локация")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


