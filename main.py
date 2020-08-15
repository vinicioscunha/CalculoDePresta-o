from calculo_prestacao import *

qtd = 0
valor_total = 0

while True:
    valor_prestacao = int(input('Digite o valor da prestação: R$ '))

    if valor_prestacao == 0:
        break

    dias = int(input('Dias de atraso: '))
    qtd = qtd + 1
    valor_total_prestacao = calculo_prestacao(valor_prestacao, dias)
    valor_total = valor_total + valor_total_prestacao
print("Quantidade de prestações: {0} \nTotal das prestações: R${1} \n".format(qtd, valor_total))
