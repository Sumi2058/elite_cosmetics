from django.db import models
from django import forms

class Product(models.Model):
  name = models.CharField(max_length=255)
  price = models.FloatField(max_length=5)
  qty=models.IntegerField(default=0)
  type=models.CharField(max_length=20)
  description=models.CharField(max_length=200)
  brand=models.CharField(max_length=200)
  mfgdate= models.DateTimeField(max_length=255,default='')
  expdate= models.DateTimeField(max_length=255,default='')
  image= models.CharField(max_length=255,default='')




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price','qty','type','description','brand','mfgdate','expdate','image']  
