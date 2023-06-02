import pytest
from decimal import Decimal
from rest_framework.test import APIClient
from banco.models import Banco

@pytest.fixture
@pytest.mark.django_db
def conta_origem():
    return Banco.objects.create(cliente="Teste 1", agencia="0001", conta=1234567, saldo=Decimal(1000))

@pytest.mark.django_db
def test_deposito_positivo(client, conta_origem):
    response = client.put(f'/banco/{conta_origem.id}/deposito/', {"valor": 100}, content_type='application/json')
    assert response.status_code == 200
    conta_origem.refresh_from_db()
    assert conta_origem.saldo == Decimal(1100)

@pytest.mark.django_db
def test_deposito_negativo(client, conta_origem):
    response = client.put(f'/banco/{conta_origem.id}/deposito/', {"valor": -100}, content_type='application/json')
    assert response.status_code == 400
    assert response.json()['error'] == "Valor de depósito não pode ser negativo."
