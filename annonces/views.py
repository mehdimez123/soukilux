from rest_framework import viewsets, permissions
from .models import Category, Announce  
from .serializers import CategorySerializer, AnnounceSerializer 


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]  # tout le monde peut voir les catégories (lecture seule)


from rest_framework import viewsets, permissions
from .models import Announce
from .serializers import AnnounceSerializer

class AnnounceViewSet(viewsets.ModelViewSet):
    queryset = Announce.objects.all()
    serializer_class = AnnounceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # ✅ Cette ligne est importante

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Announce.objects.all()
