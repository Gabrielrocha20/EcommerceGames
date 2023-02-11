from django.shortcuts import redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Produto, Variacao
from ..serializers import (ProdutoRegisterSerializer, ProdutoSerializer,
                           VariacaoSerializer)


class ProductApiList(generics.ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        ordering = self.request.query_params.get('ordering')
        if ordering == None:
            return Produto.objects.all()
        if ordering == 'price':
            ordering = 'preco_marketing'
        elif ordering == '-price':
            ordering = '-preco_marketing'
        return Produto.objects.all().order_by(ordering)

class ProductApiRegister(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoRegisterSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ProdutoRegisterSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=400)

class VariacaoApiRegister(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Variacao.objects.all()
    serializer_class = VariacaoSerializer
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        try:
            produto = Produto.objects.get(id=pk)
        except Produto.DoesNotExist:
            return Response({"error": "Produto não encontrado"}, status=404)

        serializer.save(produto=produto)

class ProdutoDeleteAPI(generics.DestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAdminUser]

class VariacaoDeleteAPI(generics.DestroyAPIView):
    queryset = Variacao.objects.all()
    serializer_class = VariacaoSerializer
    permission_classes = [IsAdminUser]


class ProductApiDetail(generics.RetrieveAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]

class VariacaoApiDetail(generics.RetrieveAPIView):
    queryset = Variacao.objects.all()
    serializer_class = VariacaoSerializer
    permission_classes = [IsAuthenticated]

class ProdutoApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoRegisterSerializer
    permission_classes = [IsAuthenticated]

class VariacaoApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = Variacao.objects.all()
    serializer_class = VariacaoSerializer
    permission_classes = [IsAdminUser]