y = 0
x = 0
robo = []

while True:
    entrada = str(input('O robo vai se mover para: '))
    robo = entrada.split(' ')
    if robo[0] == 'ESQUERDA':
        x = x - float(robo[1])
        robo.clear()
    elif robo[0] == 'DIREITA':
        x = x + float(robo[1])
        robo.clear()
    elif robo[0] == 'CIMA':
        y = y + float(robo[1])
        robo.clear()
    elif robo[0] == 'BAIXO':
        y = y - float(robo[1])
        robo.clear()
    out = str(input('Deseja parar? '))
    if out == 'S' or out == 'sim' or out == '':
        break
    else:
        continue
c1 = (x**2)
c2 = (y**2)
h = (c1 + c2)**(1/2)
print(h)