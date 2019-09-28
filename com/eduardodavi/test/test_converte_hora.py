'''
Converte hora
'''

from com.eduardodavi.converte_hora import converte_hora


def test_hora():
    '''
    Testa a hora do metodo
    '''
    converte_hora_1 = converte_hora(12, 30)
    assert converte_hora_1 == '12:30 PM', "Should be 12:30 PM"


def test_seis():
    '''
    Testa hora seis
    '''
    converte_hora_1 = converte_hora(6, 30)
    assert converte_hora_1 == '06:30 AM', "Should be 6:30 AM"


def test_seis_pm():
    '''
    testa hora seis da noite
    '''
    converte_hora_1 = converte_hora(18, 30)
    assert converte_hora_1 == '06:30 PM', "Should be 6:30 PM"


def test_meia_noite():
    '''
    testa meia noite
    '''
    meia_noite = converte_hora(0, 00)
    assert meia_noite == '12:00 AM', "Should be 12:00 am"


def test_none():
    '''
    teste none
    '''
    none_test = converte_hora(34, 30)
    assert none_test is None, "Should be 12:00 am"
