import statistics
from collections import Counter

filmes = []

def cadastrar_filme():
    nome = input("Nome do filme: ")
    genero = input("Gênero: ")
    try:
        nota = float(input("Nota (0 a 10): "))
        if nota < 0 or nota > 10:
            print("Nota inválida.")
            return
    except ValueError:
        print("Nota inválida.")
        return
    ano = input("Ano de lançamento: ")

    filme = {
        "nome": nome,
        "genero": genero,
        "nota": nota,
        "ano": ano
    }
    filmes.append(filme)
    print("Filme cadastrado com sucesso!\n")

def listar_filmes():
    if not filmes:
        print("Nenhum filme cadastrado.\n")
        return
    for i, filme in enumerate(filmes, start=1):
        print(f"{i}. {filme['nome']} | {filme['genero']} | Nota: {filme['nota']} | Ano: {filme['ano']}")
    print()

def buscar_filme():
    termo = input("Digite o nome do filme para buscar: ").lower()
    encontrados = [f for f in filmes if termo in f['nome'].lower()]
    if encontrados:
        for filme in encontrados:
            print(f"{filme['nome']} | {filme['genero']} | Nota: {filme['nota']} | Ano: {filme['ano']}")
    else:
        print("Nenhum filme encontrado com esse nome.")
    print()

def remover_filme():
    nome = input("Digite o nome do filme para remover: ").lower()
    global filmes
    novos_filmes = [f for f in filmes if f['nome'].lower() != nome]
    if len(novos_filmes) != len(filmes):
        filmes = novos_filmes
        print("Filme removido com sucesso.")
    else:
        print("Filme não encontrado.")
    print()

def exibir_estatisticas():
    if not filmes:
        print("Nenhum filme cadastrado para gerar estatísticas.\n")
        return

    total = len(filmes)
    media_nota = statistics.mean([f['nota'] for f in filmes])
    generos = [f['genero'] for f in filmes]
    genero_mais_comum = Counter(generos).most_common(1)[0][0]
    filmes_bons = [f['nome'] for f in filmes if f['nota'] >= 8]

    print(f"Total de filmes: {total}")
    print(f"Média das notas: {media_nota:.2f}")
    print(f"Gênero mais cadastrado: {genero_mais_comum}")
    print("Filmes com nota >= 8:")
    for nome in filmes_bons:
        print(f"- {nome}")
    print()

def menu():
    while True:
        print("   MENU   ")
        print("1. Cadastrar Filme")
        print("2. Listar Filmes")
        print("3. Buscar Filme")
        print("4. Remover Filme")
        print("5. Exibir Estatísticas")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")
        print()

        if opcao == '1':
            cadastrar_filme()
        elif opcao == '2':
            listar_filmes()
        elif opcao == '3':
            buscar_filme()
        elif opcao == '4':
            remover_filme()
        elif opcao == '5':
            exibir_estatisticas()
        elif opcao == '0':
            print("Encerrando")
            break
        else:
            print("Opção inválida.\n")

menu()