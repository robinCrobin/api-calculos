from modulos.calculo_imc import conta_imc
from modulos.calculo_ferias import salario, meses, conta_ferias
from modulos.calculo_rendimentos import rendimento
from modulos.calculo_parametros import parametros

def get_calculo_imc(altura, peso):
    return conta_imc(altura, peso)


def post_calculo_ferias():
    return conta_ferias(salario, meses)


def get_rendimento(invst_inicial):
    return rendimento(invst_inicial)


def get_parametros(vl1, vl2, operacao):
    return parametros(vl1, vl2, operacao)


# print(get_calculo_imc('teste',56))
#print(post_calculo_ferias())
# print(get_rendimento(3000))
get_parametros(10,2,'multiplicacao')