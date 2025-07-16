from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=250)
    username=models.CharField(max_length=250 , unique =True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    wilaya = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nom']  # nom obligatoire même si username est requis par AbstractUser

    def __str__(self):
        return f"{self.nom} - {self.email}"
