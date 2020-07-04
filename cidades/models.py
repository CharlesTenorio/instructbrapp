from django.db import models

class Cidade(models.Model):
    codigo = models.PositiveIntegerField()
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome
