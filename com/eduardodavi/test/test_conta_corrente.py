'''
Conta Corrente
'''

from com.eduardodavi.conta_corrente import ContaCorrente


def test_trocar_nome():
    '''
    Teste trocar nome
    '''
    conta = ContaCorrente(123, "x")
    conta.alterar_nome('Eduardo')
    assert conta.alterar_nome == 'Eduardo', "Deveria ser Eduardo"


def test_deposito():
    '''
    Teste deposito
    '''
    depositar = ContaCorrente(123, 'Eduardo')
    depositar.deposito(500)
    assert depositar.saldo == 500.0, "Should be 180"


def test_saque():
    '''
    Teste saque
    '''
    sacar_dinheiro = ContaCorrente(123, 'Eduardo')
    sacar_dinheiro.deposito(500)
    sacar_dinheiro.saque(320)
    assert sacar_dinheiro.saldo == 180.0, "Should be 180"
