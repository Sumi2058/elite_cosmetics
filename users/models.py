from django.db import models
from django import forms

class User(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  dob=models.CharField(max_length=20)
  gender=models.CharField(max_length=20)
  password=models.CharField(max_length=200)
  email=models.CharField(max_length=200)
  username= models.CharField(max_length=255,default='')



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname', 'lastname','dob','gender','password','email','username']  
