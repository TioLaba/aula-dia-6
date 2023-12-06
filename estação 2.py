verao = 'dezembro', 'janeiro', 'fevereiro', 'março'
outono = 'março', 'maio', 'abril','junho'
inverno = 'junho','julho', 'agosto', 'setembro'
primavera = 'setembro','outubro', 'novembro', 'dezembro'

#entrada
dia = int(input('informe o dia: '))
mês = str(input('informe o mês: '))
data =  mês
if data in outono:
    print(f'{data} é outono e se inicia dia 20 de março e vai ate 20 de junho')
elif data in verao:
    print(f'{data} é verão e se inicia dia  22 de dezembro e vai ate 20 de março')
elif data in primavera:
    print(f'{data} é primavera e se inicia dia 23 de setembro e vai ate 21 de dezembro ')
elif data in inverno:
    print(f'{data} é inverno e se inicia dia 21 de junho e vai ate 22 de setembro')
else:
    print('data invalida')
