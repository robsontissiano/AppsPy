from django.db import models


class ItemAgenda(models.Model):
	data = models.DateTimeField(auto_now_add=True)
	#hora = models.TimeField(auto_now_add=True)
	titulo = models.CharField(max_length=100)
	descricao = models.TextField()
