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

@pytest.mark.django_db
def test_saque(client, conta_origem):
    response = client.put(f'/banco/{conta_origem.id}/saque/', {"valor": 100})
    assert response.status_code == 200
    conta_origem.refresh_from_db()
    assert conta_origem.saldo == Decimal(900)

    response = client.put(f'/banco/{conta_origem.id}/saque/', {"valor": 1000})
    assert response.status_code == 400
