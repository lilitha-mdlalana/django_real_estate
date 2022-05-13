from datetime import datetime
from unicodedata import name
from django.db import models

class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now,blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self) -> str:
        return self.name
