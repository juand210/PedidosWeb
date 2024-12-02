import json
import requests
import datetime
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
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






class RegistroFacturaElectronica(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @staticmethod
    def post(request):
        try:
            jd = json.loads(request.body.decode('utf-8'))
            FNit = jd['FNit']
            FAprobado = jd['FAprobado']

            # Obtener la fecha y hora actual
            current_date = datetime.datetime.now()
            # Calcular el número de días desde una fecha de referencia (30 de diciembre de 1899)
            reference_date = datetime.datetime(1899, 12, 30)
            days_since_reference = (current_date - reference_date).days
            # Calcular la parte decimal para las horas
            decimal_hours = current_date.hour / 24 + current_date.minute / (24 * 60) + current_date.second / (
                    24 * 60 * 60)
            # Combinar los días y las horas en un solo número decimal
            decimal_value = days_since_reference + decimal_hours
            FFecha = decimal_value
            url = "http://142.4.202.90:56047/datasnap/rest/TServerMethods1/EnviarRegistro"

            dataJSON = {
                "FNit": FNit,
                "FAprobado": FAprobado,
                "FFecha": FFecha
            }
            data = {"type": "UClases.TRegistro", "id": 1, "fields": dataJSON}
            query = requests.post(url, json=data)
            if query.status_code == 200:
                response = {"Message": query.json()}
            else:
                response = {"Message": "Hubo un error en el API", "ResponseAPI": query.json()}
        except Exception as e:
            response = {"Message": str(e)}
        return JsonResponse(response, safe=False)


class RegistroMensajeria(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @staticmethod
    def post(request):
        try:
            jd = json.loads(request.body.decode('utf-8'))
            identification = jd['identification']
            name = jd['name']
            available_messages = jd['available_messages']
            origin = jd['origin']

            url = "http://10.10.10.212:8000/api/Client/"

            data = {
                "identification": identification,
                "name": name,
                "available_messages": available_messages,
                "sent_messages": 0,
                "origin": origin
            }
            query = requests.post(url, json=data)
            if query.status_code == 200:
                response = {"Message": query.json()}
            else:
                response = {"Message": query.json()}
        except Exception as e:
            response = {"Message": str(e)}
        return JsonResponse(response, safe=False)


class AdministraRecursos(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @staticmethod
    def post(request):
        try:
            ResponseAPIMessages = {}
            ResponseAPIRegister = {}
            jd = json.loads(request.body.decode('utf-8'))
            identification = jd['identification']
            identificationRegister = jd['identificationRegister']
            name = jd['name']
            available_messages = jd['available_messages']
            origin = jd['origin']
            ConsumptionApi = jd['consumption']
            Apis = ConsumptionApi.split(',')
            for Api in Apis:
                if Api == "Mensajeria":
                    url = "http://127.0.0.1:8000/api/RegistroMensajeria"
                    data = {
                        "identification": identification,
                        "name": name,
                        "available_messages": available_messages,
                        "origin": origin
                    }
                    query = requests.post(url, json=data)
                    if query.status_code == 200:
                        ResponseAPIMessages = {"ResponseAPIMessages": query.json(), "identification": identification}
                    else:
                        ResponseAPIMessages = {"ResponseAPIMessages": query.json(), "identification": identification}

                if Api == "Registro":
                    url = "http://127.0.0.1:8000/api/RegistroFacturaElectronica"
                    data = {
                        "FNit": identificationRegister,
                        "FAprobado": "True"
                    }
                    query = requests.post(url, json=data)
                    if query.status_code == 200:
                        ResponseAPIRegister = {"ResponseAPIRegister": query.json(),
                                               "identification": identificationRegister}
                    else:
                        ResponseAPIRegister = {"ResponseAPIRegister": query.json(),
                                               "identification": identificationRegister}
            # Combinar las estructuras de datos JSON
            Response = [ResponseAPIMessages, ResponseAPIRegister]

            response = {"Message": "Se Proceso el Servicio de Administracion Correctamente",
                        "ResponseAPI": Response}

        except Exception as e:
            response = {"Message": str(e)}
        return JsonResponse(response, safe=False)
