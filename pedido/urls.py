from django.urls import path

from . import views

app_name = 'pedido'
url = 'api/v1/'

urlpatterns = [
    path(f'{url}', views.PedidoApiList.as_view(), 
        name='list_api'),
    path(f'{url}<int:pk>/', views.PedidoApiDetail.as_view(), 
        name='detail_api'),
    path(f'{url}item/<int:pk>/', views.ItemPedidoApiDetail.as_view(), 
        name='item_detail_api'),

    path(f'{url}<int:pk>/pagar/', views.PagarAPIView.as_view(), 
        name='pagar_api'),

    path(f'{url}salvar/', views.SalvarPedidoAPI.as_view(), 
    name='salvar_api'),
]

