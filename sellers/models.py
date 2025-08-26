from django.db import models
from django.contrib.auth.models import User   # Import default User model
from django import forms


class Seller(models.Model):
    # Link to Django User
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sellers")

    # Business Info
    business_name = models.CharField(max_length=255)
    business_type = models.CharField(
        max_length=100,
        choices=[
            ('retail', 'Retail'),
            ('wholesale', 'Wholesale'),
            ('manufacturer', 'Manufacturer'),
            ('service', 'Service'),
        ],
        default='retail'
    )
    pan_number = models.CharField(max_length=50, blank=True, null=True)  # Tax ID

    # Address Info
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, default="Nepal")
    postal_code = models.CharField(max_length=20, blank=True, null=True)

    # Meta Info
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "sellers"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.business_name} ({self.user.username})"
    

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = [
            'user', 'business_name', 'business_type',
            'pan_number', 'address', 'city', 'state',
            'country', 'postal_code', 'is_active'
        ]
