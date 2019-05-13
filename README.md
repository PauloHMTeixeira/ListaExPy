# ListaExPy
Lista de Exercícios em Python
Essa lista de exercícios foi passada pelo professor de programação no primeiro período de cc e quis deixar aqui guardada.
Aqui vão ficar registrados os enunciados das questões.
QUESTÃO 1
Escreva um programa que calcule a raiz quadrada de um número. Utilize o método de Newton para obter um resultado aproximado. Sendo n o número a obter a raiz quadrada, considere a base b=2. Calcule p usando a fórmula p=(b+(n/b))/2. Agora, calcule o quadrado de p. A cada passo, faça b=p e recalcule p usando a fórmula apresentada. Pare quando a diferença absoluta entre n e o quadrado de p for menor que 0,0001. 


QUESTÃO 2
Um site exige que os usuários insiram nome de usuário e senha para se registrarem. Escreva um programa para verificar se a senha digitada pelos usuários é forte o suficiente.
A seguir estão os critérios para verificar a senha:

1. Pelo menos uma letra entre [a-z]
2. Pelo menos 1 número entre [0-9]
3. Pelo menos uma letra entre [A-Z]
4. Pelo menos 1 caractere de [$ # @]
5. Comprimento mínimo da senha: 6
6. Comprimento máximo da senha: 12

Seu programa deve aceitar uma sequência de senhas separadas por vírgula e as verificará de acordo com os critérios acima. As senhas que correspondem aos critérios devem ser impressas, separadas por uma vírgula.
Exemplo:
Se as seguintes senhas forem fornecidas como entrada para o programa:
ABd1234@1,a F1#,2w3E*,2We3345
Então, a saída do programa deve ser:
ABd1234@1


QUESTÃO 3
Um robô se move em um plano a partir do ponto original (0,0). O robô pode se mover nas direções CIMA, BAIXO, ESQUERDA e DIREITA de acordo com um passo fornecido. O traço do movimento do robô é mostrado da seguinte forma:

CIMA 5
BAIXO 3
ESQUERDA 3
DIREITA 2

Os números após a direção são passos. Escreva um programa para calcular a distância entre a posição atual e o ponto original após uma seqüência de movimentos. Se a distância for um float, basta imprimir o inteiro mais próximo.
Exemplo:
Se as seguintes tuplas são dadas como entrada para o programa:

CIMA 5
BAIXO 3
ESQUERDA 3
DIREITA 2

Então, a saída do programa deve ser:
2

Dicas:
As entradas devem ser lidas do console até que um valor vazio seja digitado. A saída deve ser um inteiro que representa a distancia para o ponto original. Entradas inválidas devem ser descartadas da contagem.


QUESTÃO 4
Crie uma implementação da cifra rotacional, às vezes também chamada de cifra de César. A cifra de César é uma simples cifra de deslocamento que se baseia na transposição de todas as letras do alfabeto usando uma chave inteira entre 0 e 26. O uso da chave 0 ou 26 sempre produzirá a mesma saída devido à aritmética modular. 
A letra é deslocada para tantos valores quanto o valor da chave.

A notação geral para cifras rotacionais é ROT + <chave>. A cifra rotacional mais comumente usada é a ROT13.

Um ROT13 no alfabeto latino seria o seguinte:
Normal: abcdefghijklmnopqrstuvwxyz
Cifrado: nopqrstuvwxyzabcdefghijklm

Exemplos:
Entrada: ROT5 omg 
Saída: trl
Entrada: ROT0 c 
Saída: c
Entrada: ROT26 Cool 
Saída: Cool
Entrada: ROT13 The quick brown fox jumps over the lazy dog. 
Saída: Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
Entrada: ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. 
Saída: The quick brown fox jumps over the lazy dog.

Se um valor de entrada inválido for digitado, a seguinte mensagem deve ser impressa: 'Erro'. 
Entradas inválidas podem ser entradas que contém códigos de rotações inválidos ou mensagens contendo caracteres que não estão no alfabeto. 
Exemplos:
Entrada: RARA abc Saída: Erro
Entrada: ROT5 c99 Saída: Erro

As entradas devem ser sempre compostas por ROT + <chave> + ' ' + 'mensagem', ou seja, a cifra rotacional e a mensagem a ser cifrada separados por vírgula.
  Good luck and have fun!
