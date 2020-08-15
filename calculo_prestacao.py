from calculo_multa import *
from calculo_juros import *

def calculo_prestacao(valor_prestacao, dias):
    if (dias > 0):
        valor_juros = calculo_juros(valor_prestacao, dias)
        valor_multa = calculo_multa(valor_prestacao)
        total_prestacao = valor_prestacao + valor_multa + valor_juros
        print("Valor da prestação: {0} Dias de Atraso: {1}".format(total_prestacao, dias))
        return total_prestacao 
    else:
        print("Valor da prestação: {0} Sem dias de atraso.".format(valor_prestacao))
        return valor_prestacao