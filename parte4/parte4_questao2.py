# Inicializa um dicionário para armazenar os produtos e preços
produtos = {}

while True:
    # Apresenta o menu de opções
    print("******************************** MENU ********************************")

    print("1 - Cadastrar Produto")
    print("2 - Imprimir Produtos")
    print("3 - Sair")
    print("**********************************************************************")
    # Solicita ao usuário escolher uma opção
    opcao = input("Escolha uma opção: ")


    # Verifica a opção escolhida
    if opcao == '1':
        nome_produto = input("Digite o nome do produto: ")
        preco_produto = float(input("Digite o preço do produto: R$"))
        produtos[nome_produto] = preco_produto
        print(f"Produto '{nome_produto}' cadastrado com sucesso!")

    elif opcao == '2':
        print("Produtos cadastrados:")
        for nome, preco in produtos.items():
            print(f"{nome}: R${preco:.2f}")

    elif opcao == '3':
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Escolha novamente.")