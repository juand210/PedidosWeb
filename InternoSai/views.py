import json
import requests
import datetime
from django.http import JsonResponse
from django.views import View

from InternoSai.models import Customer, Branches, Item, DocumentType, OrderHeader, OrderDetail, User
from InternoSai.serializers import (CustomerSerializers, BranchesSerializers, ItemSerializers, DocumentTypeSerializers,
                                    OrderHeaderSerializers, OrderDetailSerializers, UserSerializers)
from rest_framework import viewsets


class CustomerViewSets(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers


class BranchesViewSets(viewsets.ModelViewSet):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializers


class ItemViewSets(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers


class DocumentTypeViewSets(viewsets.ModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializers


class OrderHeaderViewSets(viewsets.ModelViewSet):
    queryset = OrderHeader.objects.all()
    serializer_class = OrderHeaderSerializers


class OrderDetailViewSets(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializers


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class AuthUser(View):
    @staticmethod
    def post(request):
        try:
            # Cargar los datos del cuerpo de la solicitud
            jd = json.loads(request.body.decode('utf-8'))
            user_name = jd.get('user_name')
            password = jd.get('password')

            # Validar que se envíen ambos campos
            if not user_name or not password:
                return JsonResponse({"Message": "El usuario y la contraseña son obligatorios."}, safe=False, status=400)

            # Buscar el usuario en la base de datos
            try:
                user = User.objects.get(user_name=user_name)
            except User.DoesNotExist:
                return JsonResponse({"Result": False, "Message": "Usuario no encontrado."}, safe=False, status=401)

            # Validar la contraseña
            if user.password == password:
                return JsonResponse({"Result": True, "Message": "Autenticación exitosa."}, safe=False, status=200)
            else:
                return JsonResponse({"Result": False, "Message": "Contraseña incorrecta."}, safe=False, status=200)

        except Exception as e:
            return JsonResponse({"Result": False, "Message": f"Error: {str(e)}"}, safe=False, status=500)
