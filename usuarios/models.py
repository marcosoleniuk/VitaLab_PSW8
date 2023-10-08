from django.contrib.auth.models import User
from django.db import models

class Cpf(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, blank=True)

    def __str__(self):
        return self.user.username
