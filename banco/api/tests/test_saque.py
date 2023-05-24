import pytest
from django.test import Client
from banco.models import Banco

client = Client()

@pytest.mark.django_db  
@pytest.mark.parametrize("saldo,valor_saque,status", [
    (100, 50, True),     # Saldo maior que o saque
    (50, 100, False),    # Saldo menor que o saque
])
def test_saque(saldo, valor_saque, status): 
    banco = Banco.objects.create(saldo=saldo, conta=1)
    response = client.post(f'/banco/{banco.id}/saque/', {'valor': valor_saque})
    assert response.status_code == 200 if status else 400
    banco.refresh_from_db()
    assert banco.saldo == saldo - valor_saque if status else saldo
    


