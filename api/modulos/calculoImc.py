class calculoImcClass: 
    def initImc():
        def getDados():
            global altura, peso 
            altura = float(input('Digite a sua altura:'))
            peso = float(input('Digite o seu peso:'))
        def calculoImc():
            global imc, peso, altura
            imc = (peso/(altura**2))
            print(f'Seu IMC é: {round(imc, 1)}')
        def classificacaoImc():
            global imc
            if imc >= 40.0:
                print('Obesidade grave')
            elif imc >= 30.0 and imc < 40.0:
                print('Obesidade')
            elif imc >= 25.0 and imc < 30.0:
                print('Sobrepeso')
            elif imc >= 18.5 and imc < 25.0:
                print('Normal')
            else:
                print('Abaixo do peso')
        getDados()
        calculoImc()
        classificacaoImc()
        