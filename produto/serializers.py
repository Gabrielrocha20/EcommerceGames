from rest_framework import serializers

from .models import Produto, Variacao


class ProdutoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(max_length=255)
    preco_marketing = serializers.FloatField()
    score = serializers.IntegerField()
    image_url = serializers.SerializerMethodField('get_image_url')
    variacoes = serializers.SerializerMethodField('get_variacoes')

    def get_variacoes(self, obj):
        query = Variacao.objects.filter(produto_id=obj.id)
        variacoes = {}
        for variacao in query:
            variacoes[variacao.nome] = f'http://localhost:8000/produtos/api/v1/variacao/{variacao.id}/'
        return variacoes

    def get_image_url(self, obj):
        if obj.imagem:
            return f"http://127.0.0.1:8000{obj.imagem.url}"
        return ''
    
    class Meta:
        model = Produto
        fields = '__all__'

class VariacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variacao
        fields = [
            "nome",
            "preco",
            "estoque",
        ]
    
class ProdutoRegisterSerializer(serializers.ModelSerializer):
    variacoes = serializers.SerializerMethodField('get_variacoes')

    def get_variacoes(self, obj):
        query = Variacao.objects.filter(produto_id=obj.id)
        print(query)
        variacoes = {}
        for variacao in query:
            variacoes[variacao.nome] = f'http://localhost:8000/produtos/api/v1/variacao/{variacao.id}/'
        return variacoes
    class Meta:
        model = Produto
        fields = '__all__'