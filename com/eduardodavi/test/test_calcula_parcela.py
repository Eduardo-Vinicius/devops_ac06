import pytest
from com.eduardodavi.calcula_parcela import valorPagamento


def test_pagamento():
	pagamento = valorPagamento(0, 2)
	assert pagamento == 0.0, "Should be None"

def test_atraso():
    pagamento = valorPagamento(20, 2)
    assert pagamento == 21.0, "Should be 21.20"

def test_sem_atraso():
    pagamento = valorPagamento(400, 0)
    assert pagamento == 400

def test_multa_adicional():
    multa = valorPagamento(25, 2)
    assert multa == 26.25, "Should be 37.5"


def test_multa_adicional2():
    multa = valorPagamento(40, 50)
    assert multa == 61.2, "Should be 61.2"

def teste_none():
    none_valor = valorPagamento(-2, 3)
    assert none_valor == None, "Inválido!"