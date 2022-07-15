from modulos import calculoImc
from modulos import calculoFerias

def getCalculoImc(altura,peso):
    print(calculoImc.contaImc(altura,peso))

def postCalculoFerias():
    salario = calculoFerias.bodyFerias['Salario']
    meses = calculoFerias.bodyFerias['Meses trabalhados']
    print(calculoFerias.contaFerias(salario,meses))

#getCalculoImc('teste',56)
postCalculoFerias()