#Un número de Lenny es un número n de cinco dígitos que cumple:

r1 = 'El número formado por los últimos dos dígitos de n es un divisor de n'
r2 = 'El primer dígito es menor al tercero'
r3 = 'El segundo dígito es mayor al quinto'
r4 = 'El cuarto dígito es menor o igual al quinto'
r5 = 'NO CUMPLE: '

while True:
    print('ingrese un numero de 5 digitos: ')
    numero = int(input())
    if len(str(numero)) == 5:
        break

c1 = numero % (numero % 100) == 0
c2 = (numero // 10000) < (numero // 100 % 10)
c3 = (numero // 1000 % 10) > (numero % 10)
c4 = (numero % 100 // 10) <= ( numero % 10)

if c1:
    print (r1)
else:
    print(r5 + r1)

if c2:
    print (r2)
else:
    print (r5 + r2)

if c3:
    print (r3)
else:
    print (r5 + r3)

if c4:
    print (r4)
else:
    print (r5 + r4)

if c1 and c2 and c3 and c4:
    print ('Numero Lenny!')
else:
    print (r5)