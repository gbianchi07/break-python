numero = int(input('Numero: '))

fatorial=1
for n in range(numero, 0 , -1):
    fatorial *= n 

print(f'fatorial de {numero} é {fatorial}')
