# GERANDO INPUTS:
a= int(input("Digite o primeiro valor: "))
b=int(input("Digite o segundo valor: "))
soma=a+b
subtração=a-b
multiplicação=a*b
divisãoF=a/b  #float
divisãoI=a/b # inteiro
resto=a%b
exponenciação=a**b

resultado=("soma: {soma} \nsubtração: {subtração}"
       " \nmultiplicação: {multiplicação} \ndivisãoF: {divisãoF}"
        "\ndivisãoI: {divisãoI} \nresto: {resto} \nexponenciação: {exponenciação}"
        .format(soma=soma, subtração=subtração, 
                multiplicação=multiplicação, divisãoF=divisãoF, divisãoI=divisãoI,
                resto=resto, exponenciação=exponenciação))  #o que está com aspas será o output (str), mas o q está entre chaves é o resultado declarado para cada função.
 
print(type(b))
print(resultado) #Realiza todas as operações com os inputs e MANTÉM os números como INTEIROS
 
print('Resultados: \n' + str(resultado)) #add o nome 'Resultados:' e converte todos os resultados(int) em str.
