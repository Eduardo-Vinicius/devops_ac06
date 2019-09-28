'''
Função que diz o valor da conta corrente
'''


class ContaCorrente:

    '''
    Classe da Conta Corrente
    '''

    def __init__(self, numero, novo_nome, saldo=0.0):
        '''
        Construtor da classe
        '''
        self.numero = numero
        self.alterar_nome = novo_nome
        self.saldo = saldo

    def alterar_nome_correntista(self, novo_nome):
        '''
        Alterar nome do correntista
        '''
        self.nome_correntista = novo_nome

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
