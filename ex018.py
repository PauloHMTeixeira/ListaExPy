alf = 'abcdefghijklmnopqrstuvwxyz'
x = input('Digite sua chave no formato ROT(chave) ')
aux = str()
y = 0
while y != len(x):
    if x[y] != ' ':
        aux = aux + x[y]
    y = y + 1
z = str()
if x[:3] != 'ROT':
    print('Erro')

elif x[3].isalnum() == False:
    print('Erro')

elif x[4] != ' ' and x[4].isalnum() == False:
    print('Erro')

elif x[4] == ' ' and aux[4:].isalpha() == False:
    print('Erro')

elif x[5] == ' ' and aux[5:].isalpha() == False:
    print('Erro')

else:
    n = str()
    n = n + x[3]
    size = len(x)
    y = 5
    posicao = alf.find(x[y].lower())
    if x[4] != ' ':
        n = n + x[4]
        y = 6
    n = int(n)

    while y != size:
        if x[y] != ' ':
            posicao = alf.find(x[y].lower())
            if posicao + n > 25:
                z = z + alf[posicao + n - 26]
            else:
                z = z + alf[posicao + n]
        else:
            z = z + ' '
        y = y + 1
print(z)