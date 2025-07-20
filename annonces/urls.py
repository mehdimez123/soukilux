from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, AnnounceViewSet, retrieve_announce_with_user

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'announces', AnnounceViewSet, basename='announce')

urlpatterns = [
    path('', include(router.urls)),
    path('announces/<uuid:announce_id>/details/', retrieve_announce_with_user, name='announce-detail'),
]
