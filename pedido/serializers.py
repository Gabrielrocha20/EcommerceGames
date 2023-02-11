from rest_framework import serializers

from .models import ItemPedido, Pedido


class PedidoSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField('get_items')

    def get_items(self, obj):
        query = ItemPedido.objects.filter(pedido_id=obj.id)
        items = {}
        for item in query:
            items[item.produto] = f'http://127.0.0.1:8000/pedido/api/v1/item/{item.id}/'
        return items
    class Meta:
        model = Pedido
        fields = [
            "id",
            "frete",
            "subtotal",
            "total",
            "qtd_total",
            "status",
            "usuario",
            "items",
        ]


class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ItemPedido
        fields = [
            "produto", 
            "produto_id", 
            "variacao", 
			"variacao_id",
			"preco",
			"quantidade",
			"imagem",
			]

class PedidoRegisterSerializer(serializers.ModelSerializer):
    items = ItemPedidoSerializer(many=True, read_only=True)
    class Meta:
        model = Pedido
        fields = [
            "id",
            "status",
            "usuario",
            "items",
        ]
    
    def create(self, validate_data):
        print(validate_data)
        pedido = Pedido.objects.create(**validate_data)
        return pedido
        

