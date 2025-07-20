from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Category, Announce
from .serializers import CategorySerializer, AnnounceSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class AnnounceViewSet(viewsets.ModelViewSet):
    queryset = Announce.objects.all()
    serializer_class = AnnounceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Announce.objects.all()


@api_view(['GET'])
def retrieve_announce_with_user(request, announce_id):
    announce = get_object_or_404(Announce, id=announce_id)
    serializer = AnnounceSerializer(announce)
    return Response(serializer.data, status=status.HTTP_200_OK)
