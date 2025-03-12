from django.db import models
from django.contrib.auth.models import AbstractUser


class DishType(models.Model):
    """Ex: dissert, pizza, pasta """
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "dish type"
        verbose_name_plural = "dish types"
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class Cook(AbstractUser):
    """Chef info"""
    years_of_experience = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Cook"
        verbose_name_plural = "Cooks"
        ordering = ["-years_of_experience"]

    def __str__(self):
        return f"{self.username} ({self.years_of_experience})"


class Dish(models.Model):
    """Ex: Napoleon, Tomato soup, Carbonara"""
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType, related_name="dishes", on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    class Meta:
        verbose_name_plural = "dishes"
        ordering = ("name",)

    def __str__(self):
        return self.name
