from django.db import models

class Meme(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    ano = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome
