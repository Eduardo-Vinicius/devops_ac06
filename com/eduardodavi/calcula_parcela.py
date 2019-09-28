'''
Função que diz os valores das multas
'''


def valorPagamento(valor, diasAtraso):
    '''
    Valor dos atrasos
    '''
    if valor < 0:
        return None
    if diasAtraso > 0:
        multa = valor * 0.03
        adicionalAtraso = valor * (diasAtraso * 0.01)
        return valor + multa + adicionalAtraso
    return valor
