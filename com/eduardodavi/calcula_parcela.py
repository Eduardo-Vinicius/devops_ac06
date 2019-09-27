def valorPagamento(valor, diasAtraso):

    if (valor < 0):
        return None
    if (diasAtraso > 0):
        multa = valor * 0.03
        adicionalAtraso = valor * (diasAtraso * 0.01)
        return valor + multa + adicionalAtraso
    else:
        return valor