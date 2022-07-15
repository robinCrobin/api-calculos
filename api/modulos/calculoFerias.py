bodyFerias = {
    'Salario': 1200.00,
    'Meses trabalhados': 4
}

def contaFerias(salario,meses):
    valor_ferias = (salario*meses)/12
    return {'Valor a ser recebido': valor_ferias}


