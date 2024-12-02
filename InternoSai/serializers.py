from rest_framework import serializers
from InternoSai.models import Customer, Branches, Item, DocumentType, OrderHeader, OrderDetail, User


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class BranchesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'


class DocumentTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = '__all__'


class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class OrderHeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderHeader
        fields = '__all__'


class OrderDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
