precoApagar = 0.0

# Pergunta se o usuário deseja pedir uma pizza
mensagem = input("Gostaria de pedir uma pizza? (sim/nao) ").strip().lower()
while mensagem not in ["sim", "nao"]:
    mensagem = input("Por favor, entre com 'sim' ou 'nao': ").strip().lower()

if mensagem == "nao":
    print("Obrigado, tenha um bom dia!")
    exit()

# Loop para processar pedidos de pizza
while True:
    # Mostrar opções de pizza
    pizza = input(
        "Escolha uma pizza:\n"
        "1 - Pizza de frango = R$33,00\n"
        "2 - Pizza de calabresa = R$120,00\n"
        "3 - Pizza brocofrango = R$43,00\n"
        "4 - Pizza lombo = R$54,00\n"
        "Digite o número da pizza que deseja: "
    ).strip()

    # Validação da escolha da pizza
    while pizza not in ["1", "2", "3", "4"]:
        pizza = input(
            "Número inválido. Escolha uma pizza:\n"
            "1 - Pizza de frango = R$33,00\n"
            "2 - Pizza de calabresa = R$120,00\n"
            "3 - Pizza brocofrango = R$43,00\n"
            "4 - Pizza lombo = R$54,00\n"
            "Digite o número da pizza que deseja: "
        ).strip()

    # Adicionar o preço da pizza escolhida ao total
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

    # Perguntar se o usuário deseja pedir mais alguma pizza
    mensagem2 = input("Deseja pedir mais alguma pizza? (sim/nao) ").strip().lower()
    while mensagem2 not in ["sim", "nao"]:
        mensagem2 = input("Por favor, entre com 'sim' ou 'nao': ").strip().lower()
    
    if mensagem2 == "nao":
        break

# Exibir o valor total a ser pago
print(f"O preço total a ser pago é: R${precoApagar:.2f}")
