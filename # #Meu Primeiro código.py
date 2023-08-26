# #Meu Primeiro código
# Autor: Ricardo
# Data: 23/08/2023


# print('Olá Mundo Ricardo')
# print('Tudo bem ?')

'''
****** Tipos de Dados ******
String = texto ex: Ricardo
______________________________________________
Number
Interger= Inteiro ex: 1 , 20, 300
Float = Fração ex: 1.4 , 3.50 , 6.8
_______________________________________________
Boolean = true or false 
print(1>=3)

'''

# ******* Variáveis **************
# Variáveis são caixas que armazenam os dados
# x= 209
# y=300
# print(x+y)

# ****** Modificando os Dados*******
# x = str("Ola")
# y= int(4)
# z= float(5)

# print(x +" "+x)
# print(y+y)
# print(z+z)

# ******** Praticando com Strings e Intergers *******
# nome= "Ricardo"
# idade= 46
# idade=str(idade)
# cidade= "Rio de Janeiro"
# print("O " + nome+ " tem " +  str(idade) + " anos " + " e mora no "+ cidade)

# ******* Adicionando Input *********
# Next class ou Próxima Aula - Vídeo 16
# nome=input("Qual é o seu nome : ")
# idade=input("Qual é a sua idade : ")
# cidade= input("Qual é a sua cidade : ")
# print("O " + nome + " tem " +  str(idade) + " anos " + " e mora em "+ cidade)

# *********** Calculando a Idade com o Input ***********
# **********  Vídeo aula 17 ************
# anoNascimento= input("Em que ano você nasceu ? ")#Aqui tem valor de String
# anoAtual=input("Em que ano estamos ? ")#Aqui tem valor de String
# idade=int(anoAtual) - int(anoNascimento)#Precisamos converter as strings em intergers
# print(idade)#O retorno foi uma interger

#******** Entendendo o Slice ***********
# ************ Vídeo Aula 18 **************
fruta = "Abacate"
print(fruta)
print(type(fruta))# Aqui vemos a classe da variável nesse exemplo é String
print(fruta[-2])#Aqui temos o index(posição) de cada, Nesdse caso temos do 0 ao 6
# A(0)(-7) - B(1)(-6) - A(2)(-5) - C(3)(-4) - A(4)(-3) - T(5)(-2) - E(6)(-1)
#Podemos ver isso com sinal negativo(-) nesse caso vai do -1 até ao -7
valor= 99.75
valor=str(valor)#Aqui tivemos que converter o interger em uma string pois o index só funciona pra STRING
print(valor[3:5])

#******** Utilizando Formated Strings  ***********
# ********Next Class - Vídeo Aula 19- Próxima Aula **************



