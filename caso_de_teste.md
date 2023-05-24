# Sacar

1. Saldo maior que zero
2. o valor que vou sacar <= saldo
3. Existe notas suficientes

##  tabela
            v             I
1. saldo |1. S > 0      |2. S = < 0
2. valor |3. V <= Saldo |4. V > Saldo
3. Notas |5. N é Sufici.|6. N não é Sufici.

##  Plano de teste

                  VS - V - N - R    VS - V - N - R     VS - V - N - R
Plano_Teste =   |(10, 5, N ➜ NO), (10, 10, N ➜ OK), (10, 0, N ➜ NO)
                |    (4, 1, 6)        (3, 1, 5)           (4,2,6)

Legenda:
VS = VALOR SAQUE | V = VALOR | N = NUMERO DE NOTAS | R = RESULTADO
---------------------------------------------------------------------------------------------------
# Depositar
1. Valor do depósito maior que zero
2. Conta bancária válida (existente)
3. Operação de depósito bem-sucedida
4. Atualização correta do saldo após o depósito


## Tabela
                 v              I
1. Valor dep  |1. V > 0       |2. V =< 0
2. Conta exi  |3. C == True   |4. C == False
3. Operação   |5. D foi feito |6. D não foi feito
4. Saldo Atual|7. S.A == S + V|8. S.A != S+V      


##  Plano de teste
                  V.D - C.E - OP - S.A - R    V.D - C.E - OP - S.A - R      V.D - C.E - OP - S.A - R 
Plano_Teste =   |( 75,   S,    S,   S ➜ OK), ( 0,   S,    N,   N ➜ NO),   (80,   N,    N,   N ➜ NO),
                |    (1, 3, 5, 7)                   (2, 3, 6, 8)                (1,3,6,8)


Legenda:
V.D = VALOR DEPOSITO | C.E = CONTA EXISTE |OP = OPERAÇÃO REALIZADA | S.A = SALDO ATUALIZADO | R = RESULTADO
---------------------------------------------------------------------------------------------------
# Transferir
1. Valor da transferência maior que zero
2. Conta de origem válida (existente)
3. Conta de destino válida (existente)
4. Saldo na conta de origem maior ou igual ao valor da transferência
5. Operação de transferência bem-sucedida
6. Atualização correta do saldo na conta de origem após a transferência
7. Atualização correta do saldo na conta de destino após a transferência


## Tabela



##  Plano de teste




Legenda:
VS = VALOR SAQUE | V = VALOR | N = NUMERO DE NOTAS | R = RESULTADO

