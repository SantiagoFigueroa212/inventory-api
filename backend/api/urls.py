from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ReviewView

router = DefaultRouter()
router.register("products", ProductViewSet)


urlpatterns = [
    *router.urls,
    path("reviews/", ReviewView.as_view()),
]