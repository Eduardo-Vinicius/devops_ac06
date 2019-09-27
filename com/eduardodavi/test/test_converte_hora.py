import pytest
from com.eduardodavi.converte_hora import converteHora


def test_hora():
	converte_hora = converteHora(12,30)
	assert converte_hora == '12:30 PM', "Should be 12:30 PM"

def test_seis():
	converte_hora = converteHora(6,30)
	assert converte_hora == '06:30 AM', "Should be 6:30 AM"

def test_seis_pm():
	converte_hora = converteHora(18,30)
	assert converte_hora == '06:30 PM', "Should be 6:30 PM"

def test_meia_noite():
	meia_noite = converteHora(0,00)
	assert meia_noite == '12:00 AM', "Should be 12:00 am"

def test_none():
	none_test = converteHora(34,30)
	assert none_test == None, "Should be 12:00 am"

