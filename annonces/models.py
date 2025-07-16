from django.db import models
import uuid
from users.models import User

# Catégorie d’annonce
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

# Annonce
class Announce(models.Model):
    PRIX_CHOICES = [
        ('OFFERT', 'Offert'),
        ('NEGOCIABLE', 'Négociable'),
        ('NON_NEGOCIABLE', 'Non négociable'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='annonces')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='annonces')
    description = models.TextField(max_length=2000, blank=False, null=False)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    prix_mode = models.CharField(max_length=50, choices=PRIX_CHOICES)
    image = models.ImageField(upload_to='announce_images/', blank=True, null=True)
    specification = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.description[:30]} - {self.prix} DA"
