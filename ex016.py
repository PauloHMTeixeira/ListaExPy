texto = input('Digite seu texto:')
senha = []
senha = texto.split(',')
tamanho = len(senha) - 1
x=[]
while tamanho >= 0:
  if any(x.isupper() for x in senha[tamanho]):
   print('Tem maiúscula')
   if any(x.islower() for x in senha[tamanho]):
      print('Tem minuscula')
      if any(x.isdigit() for x in senha[tamanho]):
         print('Tem numero')
         if senha[tamanho].count("$") > 0 or senha[tamanho].count('#') > 0 or senha[tamanho].count("@"):
            print("Tem caracteres especiais")
            if len(senha[tamanho]) >= 6 and len(senha[tamanho]) <= 12:
               print("Senha válida")
               x.append(senha[tamanho])
               tamanho = tamanho -1
            else:
                tamanho = tamanho - 1
                print("Deixe a senha com mais de 6 e menos de 12 caracteres")
         else:
             tamanho = tamanho - 1
             print("Necessario um caracter especial")
      else:
         tamanho = tamanho - 1
         print("Necessario ao menos um número")
   else:
      tamanho = tamanho - 1
      print("Necessario uma letra minuscula")
  else:
      tamanho = tamanho - 1
      print("Necessario uma letra maiuscula")
print(x)