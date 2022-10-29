from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register('product', views.ProductView)
router.register('category', views.CategoryView)

urlpatterns = [
    path('', include(router.urls)),
]