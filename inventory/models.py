from django.db import models
from django.contrib.auth.models import User


class Object(models.Model):
    slug = models.SlugField(unique=True, null=False)
    name = models.CharField(max_length=100, null=False)
    quantity = models.IntegerField(null=False)
    description = models.CharField(max_length=225, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    added = models.DateTimeField(auto_now_add=True, null=False)
    updated = models.DateTimeField(auto_now=True, null=False)
