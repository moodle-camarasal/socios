from django.db import models

# Create your models here.

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  cargo = models.CharField(max_length=255, null=True)
  correoelectronico = models.EmailField()
  phone = models.IntegerField(null=True)
  codigo_socio = models.CharField(max_length=10,null=True)
  joined_date = models.DateField(null=True)
  def __str__(self):
    return f"{self.firstname} {self.lastname}"
    
class Socios(models.Model):
    filial = models.CharField(max_length=100)
    codigo_camarasal = models.CharField(max_length=10,null=True)
    razon_social = models.CharField(max_length=80)
    persona_natural = models.CharField(max_length=80, null=True)
    estado = models.CharField(max_length=20)
    
class MisDatos(models.Model):
    AHUACHAPAN = "ah"
    SONSONATE = "so"
    SANTA_ANA = "sa"
    LA_LIBERTAD = "ll"
    CHALATENANGO = "ch"
    SAN_SALVADOR = "ss"
    CUSCATLAN = "cs"
    LA_PAZ = "lp"
    SAN_VICENTE = "sv"
    CABAÑAS = "ca"
    USULUTAN = "us"
    SAN_MIGUEL= "sm"
    MORAZAN = "mo"
    LA_UNION = "lu"
    DEPARTAMENTO_CHOICES = [
        (AHUACHAPAN, "Ahuachapán"),
        (SONSONATE, "Sonsonate"),
        (SANTA_ANA, "Santa Ana"),
        (LA_LIBERTAD, "La Libertad"),
        (CHALATENANGO, "Chalatenango"),
        (SAN_SALVADOR,"San Salvador"),
        (CUSCATLAN,"Cuscatlán"),
        (LA_PAZ,"La Paz"),
        (SAN_VICENTE,"San Vicente"),
        (CABAÑAS,"Cabañas"),
        (USULUTAN,"Usulután"),
        (SAN_MIGUEL,"San Miguel"),
        (MORAZAN,"Morazán"),
        (LA_UNION,"La Unión"),
    ]
    cargo = models.CharField(max_length=100,null=True)
    codigo = models.CharField(max_length=10,null=True)
    email = models.EmailField()
    fecha = models.DateField(null=True)
    filial = models.CharField(max_length=50,choices=DEPARTAMENTO_CHOICES,default=SAN_SALVADOR)
    nombre = models.CharField(max_length=100,null=True)
    empresa = models.CharField(max_length=100,null=True)
    registrado = models.CharField(max_length=2,null=True)
    socio = models.CharField(max_length=2,null=True)
    telefono = models.CharField(max_length=10,null=True)
    trabaja = models.CharField(max_length=2,null=True)
    usuario = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=20,null=True)

class MisCursos(models.Model):
    CC="corto"
    DD="dos"
    PP="prime"
    CORTO_ID_CHOICES = [
        (CC, "01"),
        (DD, "02"),
        (PP, "03"),
    ]
    nombre_corto = models.CharField(max_length=50,choices=CORTO_ID_CHOICES,default=CC)
    nombre_curso = models.CharField(max_length=100,null=True)
    numeral_curso = models.CharField(max_length=100,null=True)
    url_curso = models.CharField(max_length=100,null=True)
    url_producto = models.CharField(max_length=100,null=True)

class MisCorreos(models.Model):
    remitente = models.CharField(max_length=100,null=True)
    asunto = models.CharField(max_length=100,null=True)
    cuerpo = models.CharField(max_length=1000,null=True)
    otros = models.CharField(max_length=1000,null=True)
