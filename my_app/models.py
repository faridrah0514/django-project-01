from django.db import models

# Create your models here.
class CobaSatu(models.Model):
    nama = models.CharField(max_length = 100)
    alamat = models.CharField(max_length = 255)

    def __str__(self):
        return self.nama

