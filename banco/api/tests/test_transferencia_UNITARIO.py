import pytest
from decimal import Decimal
from rest_framework.test import APIClient
from banco.models import Banco

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def conta_origem():
    return Banco.objects.create(cliente="Teste 1", agencia="0001", conta="1234567", saldo=Decimal(1000))

@pytest.fixture
def conta_destino():
    return Banco.objects.create(cliente="Teste 2", agencia="0001", conta="1234568", saldo=Decimal(500))

@pytest.mark.django_db
def test_transferencia(client, conta_origem, conta_destino):
    response = client.put(f'/banco/{conta_origem.id}/transferencia/', {"valor": 100, "conta_destino_id": conta_destino.id})
    assert response.status_code == 200
    conta_origem.refresh_from_db()
    assert conta_origem.saldo == Decimal(900)
    conta_destino.refresh_from_db()
    assert conta_destino.saldo == Decimal(600)

    response = client.put(f'/banco/{conta_origem.id}/transferencia/', {"valor": 1000, "conta_destino_id": conta_destino.id})
    assert response.status_code == 400
