numero = int(input('numero: '))

cont = 0

for n in range(2, numero):
    if numero % n == 0:
        cont += 1


if cont == 0 and numero != 1:
    print('primo')
else:
    print('não é primo ')