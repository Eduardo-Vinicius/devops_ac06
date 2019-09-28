'''
Função que diz o valor da conta corrente
'''


class ContaCorrente:

    def __init__(self, numero, nome_correntista, saldo=0.0):
        '''
        Construtor da classe
        '''
        self.numero = numero
        self.alterarNome = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, nome_correntista):
        '''
        Alterar nome do correntista
        '''
        self.nomeCorrentista = nome_correntista

    def deposito(self, valor):
        '''
        Saldo apos o deposito
        '''
        self.saldo += valor

    def saque(self, valor):
        '''
        Saldo apos o saque
        '''
        self.saldo -= valor
