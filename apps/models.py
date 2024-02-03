from django.db import models

# Create your models here.


class Object(models.Model):
    """restframeworkの実験用オブジェクト
    """
    name = models.CharField(max_length=100)
    text = models.TextField()
