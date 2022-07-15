def conta_imc(altura,peso):
    #Cálculo IMC
    imc = round((peso/(altura**2)),1)
    #Classificação do cálculo
    if imc >= 40.0:
        classificacao = 'Obesidade grave'
    elif imc >= 30.0 and imc < 40.0:
        classificacao = 'Obesidade'
    elif imc >= 25.0 and imc < 30.0:
        classificacao = 'Sobrepeso'
    elif imc >= 18.5 and imc < 25.0:
        classificacao = 'Normal'
    else:
        classificacao = 'Abaixo do peso'
    #Resposta
    return {'IMC': imc, 'Classificação': classificacao}
        