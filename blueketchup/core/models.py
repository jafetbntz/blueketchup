from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

class AuditModel(models.Model):
    created_by = models.ForeignKey(User, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now = True, null=True, blank=True )
    updated_by = models.ForeignKey(User, null=True, blank=True)
    
    class Meta:
        abstract = True


class Profile(AuditModel):
    users = models.ManyToManyField(User, 'profile_id')
    tags = models.ManyToManyField(Tag, 'profile_id')
    franchises = models.ManyToManyField(Franchise, 'profile_id')

class User(User):
    sex = models.CharField(
        max_length=2,
        choices=(('M', "Masculino"), ('F', 'Femenino')),
        default='F',
    )
    profiles = models.ManyToManyField(Profile, 'user_id')


class Franchise(AuditModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    restrants = models.OneToManyField(Restaurant, 'franchise')
    profiles = models.ManyToManyField(Profile, 'franchise_id')

class Tag(AuditModel):
    name = models.CharField(max_length=50)
    restrants = models.ManyToManyField(Tag, 'tag_id')
    profiles = models.ManyToManyField(Profile, 'tag_id')

class Restaurant(AuditModel):
    name = models.CharField(max_length=50)
    franchise = models.ForeignKey(Franchise, null=True, blank=True)
    laitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(max_length=150)
    reference = models.TextField(max_length=100)
    phone = models.TextField(max_length=20)
    tags = models.ManyToManyField(Tag, 'restaurant_id')
    profiles = models.ManyToManyField(Profile, 'restaurant_id')

class Dish(AuditModel):
    name = models.CharField(max_length=50)
    franchise = models.ForeignKey(Franchise, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, null=True, blank=True)
    #profiles = models.ManyToManyField(Profile, 'dish_id')
