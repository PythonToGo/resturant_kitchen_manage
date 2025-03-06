from django.urls import path
from .views import home, DishListView, DishDetailView, DishCreateView

urlpatterns = [
    path("", home, name="home"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
]
