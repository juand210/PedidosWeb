from django.urls import path, include
from rest_framework import routers
from . import views
from InternoSai.views import AuthUser

router = routers.DefaultRouter()
router.register(r'Customer', views.CustomerViewSets, basename='Customer')
router.register(r'Branches', views.BranchesViewSets, basename='Branches')
router.register(r'Item', views.ItemViewSets, basename='Item')
router.register(r'DocumentType', views.DocumentTypeViewSets, basename='DocumentType')
router.register(r'OrderHeader', views.OrderHeaderViewSets, basename='OrderHeader')
router.register(r'OrderDetail', views.OrderDetailViewSets, basename='OrderDetail')
router.register(r'User', views.UserViewSets, basename='User')

urlpatterns = [
    path('', include(router.urls)),
    path('AuthUser', AuthUser.as_view(), name='Autenticacion de Usuario')
]
