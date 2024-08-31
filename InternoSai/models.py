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


class Item(models.Model):
    id_item = models.CharField(max_length=20, verbose_name="Codigo de articulo")
    description = models.CharField(max_length=20, verbose_name="Descripcion")
    line = models.CharField(max_length=5, verbose_name="Linea")
    group = models.CharField(max_length=5, verbose_name="Grupo")
    subgroup = models.CharField(max_length=5, verbose_name="Subgrupo")
    type = models.CharField(max_length=1, verbose_name="Identificacion")
    cost = models.FloatField(verbose_name="Costo de artículo")
    price = models.FloatField(verbose_name="Precio del articulo")
    taxed = models.IntegerField(verbose_name="Tipo de iva")
    und_sales = models.CharField(max_length=5, verbose_name="Unidad de medida para ventas")
    und_shopping = models.CharField(max_length=5, verbose_name="Unidad de medida para compras")

    def __str__(self):
        return self.description + "(" + self.id_item + ")"

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"


class DocumentType(models.Model):
    document = models.CharField(max_length=3, verbose_name="Clase documento")
    type = models.CharField(max_length=3, verbose_name="Tipo de documento")
    number = models.IntegerField(verbose_name="Consecutivo")

    def __str__(self):
        return self.document + "(" + self.type + ")"

    class Meta:
        verbose_name = "Tipo Documento"
        verbose_name_plural = "Tipo Documentos"


class OrderHeader(models.Model):
    customer = models.ForeignKey(Customer, related_name='customer', on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(DocumentType, related_name='type', on_delete=models.SET_NULL, null=True)
    number = models.IntegerField(verbose_name="Consecutivo")
    date = models.DateTimeField()
    subtotal = models.FloatField(verbose_name="Subtotal")
    taxes = models.FloatField(verbose_name="Impuestos")
    discount = models.FloatField(verbose_name="Descuento")
    total = models.FloatField(verbose_name="Total")

    def __str__(self):
        return self.customer + "(" + self.type + self.number + ")"

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"


class OrderDetail(models.Model):
    order_header = models.ForeignKey(OrderHeader, related_name='order_details', on_delete=models.CASCADE)
    product = models.ForeignKey(Item, related_name='product', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(verbose_name="Cantidad")
    price = models.FloatField(verbose_name="Precio")
    subtotal = models.FloatField(verbose_name="Subtotal")

    def __str__(self):
        return f"{self.product} - Cantidad: {self.quantity}"

    class Meta:
        verbose_name = "Detalle de Pedido"
        verbose_name_plural = "Detalles de Pedido"
