from django.db import models


class Register(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="profile_images/", null=True, blank=True)  
    
    
class Addroom(models.Model):
    roomimage = models.ImageField(upload_to="room_images/", null=True, blank=True)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    roomname = models.CharField(max_length=100, default="Unknown Room")
    bed = models.IntegerField()
    bath = models.IntegerField()
    wifi = models.CharField(max_length=3, choices=[('Yes','Yes'), ('No','No')], default='No')
    dics = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)