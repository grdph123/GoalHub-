import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('ball', 'Ball'),
        ('accessory', 'Accessory'),
        ('exclusive', 'Exclusive'),
        ('equipment', 'Equipment'),
        ('training', 'Training'),
        ('other', 'Other'),
    ]

    # Relasi ke User (pemilik produk / uploader)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # Primary key pakai UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Data produk
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    thumbnail = models.URLField(blank=True, null=True)

    # Statistik produk
    product_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    # Penanda produk
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def is_product_hot(self):
        """Produk dianggap 'hot' kalau views lebih dari 20"""
        return self.product_views > 20

    def increment_views(self):
        """Naikkan jumlah views tiap kali detail produk dilihat"""
        self.product_views += 1
        self.save()
