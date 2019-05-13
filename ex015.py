n = float(input('Diga um número: '))
b = 2
p = (b + (n / b)) / 2
q = p**2
while n - q < 0.0001:
    p = (b + (n / b)) / 2
    q = p ** 2
    b = p
    if n - q == 0:
        break
print('A sua raiz quadrada é {}' .format(p))