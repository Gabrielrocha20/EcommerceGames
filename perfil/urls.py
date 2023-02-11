from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from . import views

app_name = 'perfil'
url = 'api/v1/'

urlpatterns = [
    path(f'{url}token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{url}token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(f'{url}token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path(f'{url}login/', views.LoginAPI.as_view(), name='login_api_v1'),
    # path('register/api/v1/', views.RegisterAPI.as_view(), name='register_api_v1'),
    path(f'{url}register/perfil/', views.PerfilCreateAPI.as_view(), 
    name='perfis-create_api_v1'),

    path(f'{url}update/perfil/<int:pk>', views.PerfilUpdateAPI.as_view(), 
    name='perfis_update_api_v1'),

    path(f'{url}logout/', views.LogoutView.as_view(), name='api-logout'),
]
