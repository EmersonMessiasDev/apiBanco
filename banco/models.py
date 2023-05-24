from django.db import models
from django.contrib.auth.models import User

class Banco(models.Model):
    cliente = models.CharField(max_length=20)
    agencia = models.CharField(max_length=10)
    conta = models.IntegerField(null=False)
    saldo = models.DecimalField(max_digits=11,decimal_places=2)
    
    def __str__(self) -> str:
        return self.cliente
    

    
    
    