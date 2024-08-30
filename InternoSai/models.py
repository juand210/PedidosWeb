from django.db import models


# Create your models here.

class Customer(models.Model):
    identification = models.CharField(max_length=20, verbose_name="Identificacion", unique=True)
    name = models.CharField(max_length=50, verbose_name="Nombres")
    last_name = models.CharField(max_length=50, verbose_name="Apellidos")
    company_name = models.CharField(max_length=50, verbose_name="Nombre Compañia")
    document_type = models.IntegerField(verbose_name="Tipo de Documento")
    taxpayer_type = models.IntegerField(verbose_name="Tipo de Contribuyente")
    address = models.CharField(max_length=50, verbose_name="Direccion")
    phone = models.CharField(max_length=20, verbose_name="Telefono")
    email = models.CharField(max_length=50, verbose_name="Email")
    country = models.CharField(max_length=20, verbose_name="Pais")
    departament = models.CharField(max_length=20, verbose_name="Departamento")
    city = models.CharField(max_length=20, verbose_name="Ciudad")

    def __str__(self):
        return self.name + "(" + self.identification + ")"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Branches(models.Model):
    id_branche = models.IntegerField(verbose_name="codigo de sucursal")
    identification = models.CharField(max_length=20, verbose_name="Identificacion")
    name = models.CharField(max_length=50, verbose_name="Nombres")
    last_name = models.CharField(max_length=50, verbose_name="Apellidos")
    company_name = models.CharField(max_length=50, verbose_name="Nombre Compañia")
    document_type = models.IntegerField(verbose_name="Tipo de Documento")
    taxpayer_type = models.IntegerField(verbose_name="Tipo de Contribuyente")
    address = models.CharField(max_length=50, verbose_name="Direccion")
    phone = models.CharField(max_length=20, verbose_name="Telefono")
    email = models.CharField(max_length=50, verbose_name="Email")
    country = models.CharField(max_length=20, verbose_name="Pais")
    departament = models.CharField(max_length=20, verbose_name="Departamento")
    city = models.CharField(max_length=20, verbose_name="Ciudad")

    def __str__(self):
        return self.name + "(" + self.identification + ")"

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
