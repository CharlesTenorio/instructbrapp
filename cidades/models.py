from django.db import models

class Uf(models.Model):
    prefixo = models.CharField(max_length=2, primary_key=True)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.uf

class Cidade(models.Model):
    codigo_ibge = models.CharField(max_length=20, primary_key=True)
    codito_uf = models.ForeignKey(Uf, on_delete=models.PROTECT)
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome
