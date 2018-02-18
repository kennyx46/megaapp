from django.db import models

class Site(models.Model):
    name = models.CharField(max_length=50)

class Detail(models.Model):
    a = models.FloatField(default=0.00)
    b = models.FloatField(default=0.00)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)