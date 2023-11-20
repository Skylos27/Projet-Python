from django.db import models

class Password(models.Model):
    id = models.IntegerField(primary_key=True,max_length=100,editable=False)
    site_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    sharedTo = models.CharField( max_length=100)
    owner = models.CharField(max_length=100)