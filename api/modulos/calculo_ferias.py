
body_ferias = {
    'Salario': 1200.00,
    'Meses trabalhados': 4
}

salario = body_ferias['Salario']
meses = body_ferias['Meses trabalhados']

def conta_ferias(salario,meses):
    valor_ferias = (salario*meses)/12
    return {'Valor a ser recebido': valor_ferias}


