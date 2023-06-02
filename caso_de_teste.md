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



## Tabela
                 v              I
1. Valor dep  |1. V > 0       |2. V =< 0
2. Conta exi  |3. C == True   |4. C == False
    


##  Plano de teste
                  V.D - C.E  - R    V.D - C.E  - R      V.D - C.E  - R 
Plano_Teste =   |( 75,   S,  ➜ OK), ( 0,   S,  ➜ NO),   (80,   N, ➜ NO),
                |    (1, 3,)            (2, 3,)                (1,3)


Legenda:
V.D = VALOR DEPOSITO | C.E = CONTA EXISTE |OP = OPERAÇÃO REALIZADA | S.A = SALDO ATUALIZADO | R = RESULTADO
---------------------------------------------------------------------------------------------------
# Transferir
1. Valor da transferência maior que zero
2. Conta de origem válida (existente)
3. Conta de destino válida (existente)
4. Saldo na conta de origem maior ou igual ao valor da transferência


## Tabela
                 v              I
1. Valor tra    |1. V > 0       |2. V =< 0
2. Conta D exi  |3. C.D == True |4. C.D == False
3. Conta O exi  |5. C.O == True |6. C.O == False
4. Saldo O      |7. S.O >= V.T  |8. S.O <= V.T  


##  Plano de teste
                  V.T - S.O  - C.O - C.D  - R       V.T - S.O  - C.O - C.D  - R      V.T - S.O  - C.O - C.D  - R
Plano_Teste =   |( 100,  200,  True,  True ➜ OK), ( 520, 510, True,  True  ➜ NO), (250, 250, True,  False ➜ NO ),
                |      (1, 7, 5, 3)                        (1, 8, 5, 3)                (1, 7 , 5, 4)


Legenda:
VT = VALOR TRANFERENCIA | S.O = SALDO ORIGEM | C.O = CONTA ORIGEM | C.D = CONTA DESTINO

