from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer, RegisterSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            refresh = RefreshToken.for_user(user)

            return Response({
                "message": "Connexion réussie ✅",
                "user": {
                    "id": str(user.id),
                    "nom": user.nom,
                    "email": user.email,
                },
                "tokens": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            return Response({
                "message": "Compte créé avec succès ✅",
                "user": {
                    "id": str(user.id),
                    "nom": user.nom,
                    "email": user.email,
                },
                "tokens": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# Dans annonces/views.py ou users/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['GET'])
def get_user_details(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        return Response({
            'id': str(user.id),
            'nom': user.nom,
            'username': user.username,
            'email': user.email,
            'phone_number': user.phone_number,
            'wilaya': user.wilaya,
            'commune': user.commune,
        })
    except User.DoesNotExist:
        return Response({'error': 'Utilisateur non trouvé'}, status=404)