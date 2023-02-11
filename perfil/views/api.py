from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from rest_framework import authentication, generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,
                                   HTTP_404_NOT_FOUND)

from ..models import Perfil
from ..serializers import (PerfilSerializer, UserRegisterSerializer,
                           UserSerializer)


class LoginAPI(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        return Response({'success': 'Login successful'}, status=HTTP_200_OK)

class LogoutView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        logout(request)
        return Response({'status': 'ok'})

class UserCreateAPI(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    # permission_classes = [IsAuthenticated]
class PerfilCreateAPI(generics.CreateAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        try:
            usuario = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({"error": "User não encontrado"}, status=404)

        serializer.save(usuario=usuario)

class PerfilUpdateAPI(generics.RetrieveUpdateAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    # permission_classes = [IsAuthenticated]
