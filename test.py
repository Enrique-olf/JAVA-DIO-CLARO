#o codigo deve começar com uma decisao de pedir uma pizza ou nao
#printar os tipos de pizza disponiveis 4
#permitir ao usuario digitar qual pizza deseja
#questionar se ele deseja pedir mais alguma coisa
#printar valor a ser pago
precoApagar = 0.0
mensagem2 = ""
mensagem = input("Gostaria de pedir uma pizza? ")
while mensagem != "nao" and mensagem != "sim": mensagem = input("Gostaria de pedir uma pizza? Entre com sim ou nao: ")
if mensagem == "nao" : exit("Obrigado tenha um bom dia!")
else: pizza = input("1-pizza de frango = 33,00 \n 2-pizza de calabreza = 120,00 \n 3-pizza brocofrango = 43,00 \n 4-pizza lombo = 54,00 \n digite o numero da pizza que deseja: ") 
while pizza != "1" and pizza != "2" and pizza != "3" and pizza != "4" : pizza = input ('digite um numero valido referente a pizzas: \n 1-pizza de frango = 33,00 \n 2-pizza de calabreza = 120,00 \n 3-pizza brocofrango = 43,00 \n 4-pizza lombo = 54,00 \n digite o numero da pizza que deseja: ')
if pizza == "1":
 precoApagar += 33.00
 print("Pizza de frango = R$33,00")
elif pizza == "2":
 precoApagar += 120.00
 print("Pizza de calabresa = R$120,00")
elif pizza == "3":
 precoApagar += 43.00
 print("Pizza brocofrango = R$43,00")
elif pizza == "4":
 precoApagar += 54.00
 print("Pizza lombo = R$54,00")
else:print("Número de pizza inválido. digite sim ou nao.")
mensagem2 = input ("deseja pedir mais alguma pizza? ")
while mensagem2 != "nao" and mensagem2 != "sim" : mensagem2 = input ("digite sim ou náo seu burro! ")
if mensagem2 == "sim" :
   for i in range(100):
     pizza = input("1-pizza de frango = 33,00 \n ,2-pizza de calabreza = 120,00 \n , 3-pizza brocofrango = 43,00 \n , 4-pizza lombo = 54,00 \n ,  digite o numero da pizza que deseja: ")                     
     while pizza != "1" and pizza != "2" and pizza != "3" and pizza != "4" : pizza = input ('digite um numero valido refe3rente a pizzas: \n 1-pizza de frango = 33,00 \n 2-pizza de calabreza = 120,00 \n 3-pizza brocofrango = 43,00 \n 4-pizza lombo = 54,00 \n digite o numero da pizza que deseja: ')
     if pizza == "1": precoApagar += float(33.00) , print("Pizza de frango = R$33,00")
     elif pizza == "2": precoApagar += float(120.00) , print("Pizza de calabresa = R$120,00")
     elif pizza == "3": precoApagar += float(43.00) , print("Pizza brocofrango = R$43,00")
     elif pizza == "4": precoApagar += float(54.00) , print("Pizza lombo = R$54,00")
     else:
        print("Número de pizza inválido. Tente novamente.")
        mensagem2 = input ("deseja pedir mais alguma pizza? ")
        while mensagem2 != "nao" and mensagem2 != "sim" : mensagem2 = input ("digite sim ou náo seu burro! ")
     if mensagem2 == "nao":
        break
print(f"O preço total é: R${float(precoApagar):.2f}")