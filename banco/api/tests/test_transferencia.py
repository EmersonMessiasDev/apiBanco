import pytest
from django.test import Client
from banco.models import Banco

client = Client()

@pytest.mark.django_db
def test_transferencia():
    # Create the Banco objects for testing
    banco_origem = Banco.objects.create(saldo=100, conta=1)
    banco_destino = Banco.objects.create(saldo=0, conta=2)
    
    # Define the transferencia parameters
    valor_transferencia = 50
    conta_destino_id = banco_destino.id
    
    # Make a POST request to perform the transferencia
    response = client.post(f'/banco/{banco_origem.id}/transferencia/', {'valor': valor_transferencia, 'conta_destino_id': conta_destino_id}, format='json')
    
    # Assert the response status code is 200, indicating a successful transferencia
    assert response.status_code == 200
    
    # Refresh the banco_origem and banco_destino objects from the database
    banco_origem.refresh_from_db()
    banco_destino.refresh_from_db()
    
    # Assert the saldo update in banco_origem
    assert banco_origem.saldo == 100 - valor_transferencia
    
    # Assert the saldo update in banco_destino
    assert banco_destino.saldo == valor_transferencia