from django.urls import path

from .views import api

app_name = 'produto'

url = 'api/v1/'

urlpatterns = [
     # Apis View
     path(
     url, api.ProductApiList.as_view(), name='product_api_v1'
     ),
     path(
          f"{url}<int:pk>/",
          api.ProductApiDetail.as_view(), name='product_detail_api_v1'
     ),
     path(
          f"{url}variacao/<int:pk>/",
          api.VariacaoApiDetail.as_view(), name='variacao_detail_api_v1'
     ),
     # Apis Register
     path(
          f"{url}register/", api.ProductApiRegister.as_view(),
          name='product_register_api_v1'
     ),
     path(
          f"{url}register/variacao/<int:pk>/", api.VariacaoApiRegister.as_view(),
          name='variacao_register_api_v1'
     ),

     #Apis Delete
     path(f"{url}delete/variacoes/<int:pk>/", api.VariacaoDeleteAPI.as_view(), 
     name='variacao-delete_api_v1'),

     path(f"{url}delete/<int:pk>/", api.ProdutoDeleteAPI.as_view(), 
     name='produto-delete_api_v1'),

     #Apis Update
     path(f"{url}update/variacoes/<int:pk>/", api.VariacaoApiUpdate.as_view(), 
     name='variacao-update_api_v1'),

     path(f"{url}update/<int:pk>/", api.ProdutoApiUpdate.as_view(), 
     name='produto-update_api_v1'),
]
