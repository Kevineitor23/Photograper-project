from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Usuarios(models.Model):
    name = models.CharField(max_length = 100, )
    date = models.DateTimeField(auto_now_add = True)
    dificultad = models.CharField(max_length = 25)

    def get_name(self):
        return self.name, self.date, 

    order_by = ['created']


class Contacto(models.Model):
    name = models.CharField(max_length = 200)
    motivo = models.CharField(max_length = 250)    
    phoneNumber = PhoneNumberField(unique = True)

