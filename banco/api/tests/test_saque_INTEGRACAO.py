import pytest
from django.test import Client
from banco.models import Banco

client = Client()

@pytest.mark.django_db  
@pytest.mark.parametrize("saldo,valor_saque,status", [
    (100, "50", True),     # Saldo maior que o saque
    (50, "100", False),    # Saldo menor que o saque
])
def test_saque(saldo, valor_saque, status): 
    banco = Banco.objects.create(saldo=saldo, conta=1, cliente='test', agencia='001')
    response = client.put(f'/banco/{banco.id}/saque/', {'valor': valor_saque}, content_type='application/json')
    assert response.status_code == 200 if status else 400
    banco.refresh_from_db()
    assert float(banco.saldo) == float(saldo) - float(valor_saque) if status else float(saldo)



