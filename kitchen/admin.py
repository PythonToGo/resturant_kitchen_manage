from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import DishType, Cook, Dish

@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldssets = UserAdmin.fieldsets + (
        (("Additional Info", {"fields": ("years_of_experience",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional Info",
                {
                    "fiedls": (
                        "first_name",
                        "last_name",
                        "years_of_experience",
                    )
                },
            ),
        )
    )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "dish_type", "description",)
    list_filter = ("dish_type", "price",)
    search_fields = ("name",)
    