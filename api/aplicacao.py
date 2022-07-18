from modulos.calculo_imc import conta_imc
from modulos.calculo_ferias import conta_ferias
from modulos.calculo_rendimentos import fun_rendimento
from modulos.calculo_parametros import parametros

event = {
  "queryStringParameters": {
    'altura': 1.56,
    'peso': 48,
    'rendimento': 3000,
    'valor1': 40,
    'valor2': 20,
    'calculo': 'subtracao'
  },
  "pathParameters": {
    "valor-rendimento": 1000
  },
 
  "body": {'Salário': 1200.00,
  'Meses trabalhados': 4} ,
}

def get_calculo_imc(event, context):
    query_parametros = event['queryStringParameters']
    altura = query_parametros['altura']
    peso = query_parametros['peso']

    return conta_imc(altura, peso)

def post_calculo_ferias(event, context):
    body = event['body']
    salario = body['Salário']
    meses = body['Meses trabalhados']

    return conta_ferias(salario, meses)

def get_rendimento(event, context):
    path_parametro = event['pathParameters']
    rendimento = path_parametro['valor-rendimento']

    return fun_rendimento(rendimento)

def get_parametros(event, context):
    query_parametros = event['queryStringParameters']
    valor1 = query_parametros['valor1']
    valor2 = query_parametros['valor2']
    calculo = query_parametros['calculo']

    return parametros(valor1, valor2, calculo)

print(get_calculo_imc(event, 0))
print(post_calculo_ferias(event, 0))
print(get_rendimento(event, 0))
print(get_parametros(event, 0))