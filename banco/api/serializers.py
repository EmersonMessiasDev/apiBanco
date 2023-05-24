from rest_framework.serializers import ModelSerializer
from banco.models import Banco

class BancoSerializers(ModelSerializer):
    class Meta:
        model = Banco
        fields = ['id','cliente', 'agencia', 'conta','saldo']
        
