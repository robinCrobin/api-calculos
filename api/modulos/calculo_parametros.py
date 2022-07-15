def parametros(vl1,vl2,operacao):
    def soma():
        return {
            'Tipo': operacao,
            'Resultado': vl1+vl2
        }
    def subtracao():
        return {
            'Tipo': operacao,
            'Resultado': vl1-vl2
        }
    def divisao():
        return {
            'Tipo': operacao,
            'Resultado': vl1/vl2
        }
    def multiplicacao():
        return {
            'Tipo': operacao,
            'Resultado': vl1*vl2
        }
    def default():
        return 'Não foi possível identificar o tipo de cálculo'

    lst_operacoes = dict.fromkeys(['soma','Soma'], soma)
    lst_operacoes.update(dict.fromkeys(['multiplicacao','multiplicaçao','multiplicacão','multiplicação','Multiplicacao','Multiplicaçao','Multiplicão','Multiplicação'], multiplicacao))
    lst_operacoes.update(dict.fromkeys(['subtracao','subtraçao','subtracão','subtração','Subtracao','Subtraçao','Subtracão','Subtração'], subtracao))
    lst_operacoes.update(dict.fromkeys(['divisao','divisão','Divisao','Divisão'],divisao))

    def verificar_operacao(operacao):
        return lst_operacoes.get(operacao, default)()

    print(verificar_operacao(operacao))
