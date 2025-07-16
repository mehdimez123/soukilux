from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, AnnounceViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'announces', AnnounceViewSet, basename='announce')

urlpatterns = [
    path('', include(router.urls)),
]
