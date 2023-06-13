from django.db import models

# Create your models here.
class Kayakista(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    ubicacion = models.CharField(max_length=40)
    club = models.CharField(max_length=40)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - E-Mail {self.email} - Ubicación {self.ubicacion} - Club {self.club}"




class Club(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    localidad = models.CharField(max_length=40)
    provincia = models.CharField(max_length=40, default="")
    pais = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.nombre} - Email:  {self.email} - Localidad: {self.localidad} - Provincia: {self.provincia}- Pais: {self.pais}"




class Travesia(models.Model):
    kayakista = models.CharField(max_length=40)
    email = models.EmailField(default="")
    partida = models.CharField(max_length=40)
    distancia = models.CharField(max_length=40)
    fecha = models.CharField(max_length=500)
    
    def __str__(self):
        return f"- Kayakista: {self.kayakista} \n- Email: {self.email} \n- Partida: {self.partida}\n- Distancia: {self.distancia} \n- Fecha: {self.fecha}"