import pytest
from django.test import Client
from banco.models import Banco

client = Client()


@pytest.mark.django_db
@pytest.mark.parametrize("saldo, valor_deposito, status", [
    (100, "150", True),     # Depósito bem-sucedido
    (100, "0", False),     # Depósito de valor zero
    (100, "-50", False),   # Depósito de valor negativo
])
def test_deposito(saldo, valor_deposito, status):
    banco = Banco.objects.create(saldo=saldo, conta=1, cliente='test', agencia='001')
    response = client.put(f'/banco/{banco.id}/deposito/', {'valor': valor_deposito}, content_type='application/json')
    assert response.status_code == 200 if status else 400
    banco.refresh_from_db()
    assert float(banco.saldo) == float(saldo) + float(valor_deposito) if status else float(saldo)






