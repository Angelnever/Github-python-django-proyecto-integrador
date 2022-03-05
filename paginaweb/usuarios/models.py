from django.db import models

# reate your models here.
class Usuario(models.Model):
    id= models.AutoField(primary_key=True)
    Usuario = models.CharField(max_length=50, verbose_name='usuario',)
    Nombre = models.CharField(max_length=50, verbose_name='nombre')
    Apellido = models.CharField(max_length=50, verbose_name='apellido')
    Password = models.CharField(max_length=50, verbose_name='password')
    Direccion = models.CharField(max_length=50, verbose_name='direccion')
    Email = models.EmailField(max_length=50, verbose_name='email')
    Telefono = models.CharField(max_length=11, verbose_name='telefono')
     
    
def __str__(self):
    fila = "usuario: " + self.Usuario + "-" + "email: " + self.Email
    return fila
   
