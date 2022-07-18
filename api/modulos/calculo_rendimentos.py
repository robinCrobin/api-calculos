def fun_rendimento(invst_inicial):
    vl_final = round((invst_inicial * 1.05),2)
    return {
        'Investimento inicial': invst_inicial,
        'Valor final': vl_final
    }