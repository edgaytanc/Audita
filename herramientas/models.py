from django.db import models
from django.contrib.auth.models import User

class Firma(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firma = models.BinaryField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Firma de {self.user.username}"
    
