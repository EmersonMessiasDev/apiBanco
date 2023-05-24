import decimal
from requests import Response
from rest_framework.viewsets import ModelViewSet
from banco.models import Banco
from .serializers import BancoSerializers
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from decimal import Decimal

class BancoViewSet(ModelViewSet):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializers
    
    
    @action(detail=True, methods=['post'])
    def deposito(self, request, pk=None):
        banco = self.get_object()
        serializer = self.get_serializer(banco)
        
        valor = request.data.get('valor')
        if valor is None:
            return Response({'error': 'Informe o valor para o depósito.'}, status=status.HTTP_400_BAD_REQUEST)
        
        banco.saldo += Decimal(str(valor))
        banco.save()
        
        return Response(serializer.data)



    @action(detail=True, methods=['post'])
    def saque(self, request, pk=None):
        banco = self.get_object()
        serializer = self.get_serializer(banco)
        
        valor = request.data.get('valor')
        if valor is None:
            return Response({'error': 'Informe o valor para o saque.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if banco.saldo >= Decimal(str(valor)):
            banco.saldo -= Decimal(str(valor))
            banco.save()
        else:
            return Response({'error': 'Saldo insuficiente.'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data)



    @action(detail=True, methods=['post'])
    def transferencia(self, request, pk=None):
        banco_origem = self.get_object()
        serializer = self.get_serializer(banco_origem)
        
        valor = request.data.get('valor')
        conta_destino_id = request.data.get('conta_destino_id')
        
        if valor is None or conta_destino_id is None:
            return Response({'error': 'Informe o valor e a conta de destino para a transferência.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            conta_destino = Banco.objects.get(id=conta_destino_id)
        except Banco.DoesNotExist:
            return Response({'error': 'Conta de destino não encontrada.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if banco_origem.saldo >= Decimal(str(valor)):
            banco_origem.saldo -= Decimal(str(valor))
            banco_origem.save()
            conta_destino.saldo += Decimal(str(valor))
            conta_destino.save()
        else:
            return Response({'error': 'Saldo insuficiente.'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data)