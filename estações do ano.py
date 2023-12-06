#preciso de duas entrada de funções ( mes, dia )
#preciso que essas duas entradas me informem a estação atual

#apresentação
print('Seja bem vindo')
#definir função dia = vai informar a data e me vai retornar

dia = (int(input('que dia é hoje ? : ')))
mes = (str(input('Que mes estamos: ')))
lista_dia = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
             15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
             27, 28, 29, 30, 31)
lista_mes = ('janeiro', 'feveiro', 'março', 'abril', 'maio', 'junho',
             'julho', 'agosto', 'setembro', 'outubro', 'novembro','dezembro' )

#criar função dia que recebe a entrada do usuario
# e verifica se o numero esta dentro da lista

if dia in lista_dia:
    dia == lista_dia

else:
    lista_dia != dia
    print(f'{dia} o numero é invalido(tah certo tambem')

if mes in lista_mes:
    mes == lista_mes

else:
    lista_mes != mes
    print(f'{mes} o numero é invalido(tah certo tambem')

#agora eu posso converter as duas funçoes em duas variaveis
diaestacao = dia
mesestacao = mes
print(f'{diaestacao} de {mesestacao} é dia de signo : ')

lista_estacao = ('{primavera},{outono}, {inverno}, {primavera}')

primavera = (f'{lista_mes[8 : 13]},{lista_dia[ 0 : 32]}')
if dia and mes:

 print(f'{primavera}')









# agora eu tenho que criar funções dentro do dia = ele vai ter que me informar
# qual é o dia(valor inserido pelo usuario) que estamos e se ele é igual o da
# lista do calendario
# qual é o mes(valor inserido pelo usuario) que estamos e se ele é igual o da
# lista de calendario



