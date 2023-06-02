from django.test import TestCase
import pytest
from banco.models import Banco
from decimal import Decimal
from rest_framework import status
# client = Client()

from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_valor_transferencia_maior_que_zero():
    # Cria os objetos Banco para teste
    banco_origem = Banco.objects.create(saldo=100, conta=1, cliente='test', agencia='001')
    banco_destino = Banco.objects.create(saldo=0, conta=2, cliente='test', agencia='002')

    # Define os parâmetros da transferência
    valor_transferencia = -50  # Mudado de "-50" (string) para -50 (int)

    # Faz uma requisição PUT para realizar a transferência
    response = client.put(f'/banco/{banco_origem.id}/transferencia/', {'valor': valor_transferencia, 'conta_destino_id': banco_destino.id}, content_type='application/json')

    # Afirma que o código de status da resposta é 400, indicando uma falha na transferência devido a valor negativo
    assert response.status_code == 400


@pytest.mark.django_db
def test_conta_origem_valida():
    # Supondo que a conta com id 999 não exista
    invalid_account_id = 999

    # Define os parâmetros da transferência
    valor_transferencia = "50"

    # Faz uma requisição PUT para realizar a transferência com uma conta de origem inválida
    response = client.put(f'/banco/{invalid_account_id}/transferencia/', {'valor': valor_transferencia, 'conta_destino_id': 2}, content_type='application/json')
    print(response)
    # Afirma que o código de status da resposta é 404, indicando uma falha na transferência devido à conta de origem inválida
    assert response.status_code == 404

@pytest.mark.django_db
def test_conta_destino_valida():
    # Cria os objetos Banco para teste
    banco_origem = Banco.objects.create(saldo=100, conta=1, cliente='test', agencia='001')

    # Supondo que a conta com id 999 não exista
    invalid_account_id = 999

    # Define os parâmetros da transferência
    valor_transferencia = "50"

    # Faz uma requisição PUT para realizar a transferência com uma conta de destino inválida
    response = client.put(f'/banco/{banco_origem.id}/transferencia/', {'valor': valor_transferencia, 'conta_destino_id': invalid_account_id}, content_type='application/json')

    # Afirma que o código de status da resposta é 400, indicando uma falha na transferência devido à conta de destino inválida
    assert response.status_code == 400

@pytest.mark.django_db
def test_saldo_suficiente_na_conta_origem():
    # Cria os objetos Banco para teste com saldo menor que o valor da transferência
    banco_origem = Banco.objects.create(saldo=20, conta=1, cliente='test', agencia='001')
    banco_destino = Banco.objects.create(saldo=0, conta=2, cliente='test', agencia='002')

    # Define os parâmetros da transferência
    valor_transferencia = "50"

    # Faz uma requisição PUT para realizar a transferência
    response = client.put(f'/banco/{banco_origem.id}/transferencia/', {'valor': valor_transferencia, 'conta_destino_id': banco_destino.id}, content_type='application/json')

    # Afirma que o código de status da resposta é 400, indicando uma falha na transferência devido ao saldo insuficiente
    assert response.status_code == 400


class TransferenciaTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.origem = Banco.objects.create(saldo=100, conta=1, cliente='test', agencia='001')
        self.destino = Banco.objects.create(saldo=0, conta=2, cliente='test', agencia='002')

    def test_atualizacao_saldo_conta_origem(self):
        data = {
            'valor': '50.00',
            'conta_destino_id': self.destino.id,
        }
        response = self.client.put(f'/banco/{self.origem.id}/transferencia/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.origem.refresh_from_db()
        self.assertEqual(self.origem.saldo, Decimal('50.00'))


    def test_atualizacao_saldo_conta_destino(self):
        data = {
            'valor': '50.00',
            'conta_destino_id': self.destino.id,
        }
        response = self.client.put(f'/banco/{self.origem.id}/transferencia/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.destino.refresh_from_db()
        self.assertEqual(self.destino.saldo, Decimal('50.00'))
