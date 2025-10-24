import os
import time
import uuid
import json

# Caminhos para os arquivos de salvamento
ARQUIVO_POKEDEX = "pokedex.json"
ARQUIVO_POKEMONS = "pokemons_disponiveis.json"

# Funções de salvamento e carregamento
def salvar_dados():
    with open(ARQUIVO_POKEDEX, "w", encoding="utf-8") as f:
        json.dump(pokedex, f, indent=4, ensure_ascii=False)
    with open(ARQUIVO_POKEMONS, "w", encoding="utf-8") as f:
        json.dump(pokemons_disponiveis, f, indent=4, ensure_ascii=False)

def carregar_dados():
    global pokedex, pokemons_disponiveis
    if os.path.exists(ARQUIVO_POKEDEX):
        with open(ARQUIVO_POKEDEX, "r", encoding="utf-8") as f:
            pokedex = json.load(f)
    else:
        pokedex = []

    if os.path.exists(ARQUIVO_POKEMONS):
        with open(ARQUIVO_POKEMONS, "r", encoding="utf-8") as f:
            pokemons_disponiveis = json.load(f)
    else:
        pokemons_disponiveis = [
            {"nome": "Pikachu", "tipo": "Elétrico"},
            {"nome": "Charmander", "tipo": "Fogo"},
            {"nome": "Bulbasaur", "tipo": "Planta/Veneno"},
            {"nome": "Squirtle", "tipo": "Água"},
            {"nome": "Eevee", "tipo": "Normal"},
            {"nome": "Jigglypuff", "tipo": "Fada"},
            {"nome": "Gengar", "tipo": "Fantasma/Veneno"}
        ]

# Sistema de boas-vindas
def boas_vindas():
    os.system("cls" if os.name == "nt" else "clear")
    print("Bem-vindo ao Mundo Pokémon!")
    nome = input("Antes de começar, qual é o seu nome, treinador? ")
    print(f"\nSeja bem-vindo, {nome.title()}! Sua jornada Pokémon começa agora!")
    time.sleep(2)
    return nome

# Exibição do menu
def exibir_menu():
    print("\nMENU PRINCIPAL")
    print("1 - Ver Pokédex completa")
    print("2 - Capturar Pokémon")
    print("3 - Remover Pokémon da Pokédex")
    print("4 - Adicionar novo Pokémon manualmente")
    print("5 - Sair da Pokédex")
    print("\n(Digite 'menu' para voltar a qualquer momento.)")

# Ver Pokédex
def ver_pokedex():
    print("\nSua Pokédex:")
    for p in pokemons_disponiveis:
        capturado = next((pk for pk in pokedex if pk["nome"].lower() == p["nome"].lower()), None)
        if capturado:
            print(f"{p['nome']} | Tipo: {p['tipo']} | ID: {capturado['id']}")
        else:
            print(f"{p['nome']} | BLOQUEADO")
    input("\n(Pressione Enter para voltar ao menu)")

# Capturar Pokémon
def capturar_pokemon():
    print("\nPokémons disponíveis para captura:")
    for p in pokemons_disponiveis:
        capturado = any(pk["nome"].lower() == p["nome"].lower() for pk in pokedex)
        status = "Capturado" if capturado else "Disponível"
        print(f"- {p['nome']} ({p['tipo']}) [{status}]")

    nome = input("\nDigite o nome do Pokémon que deseja capturar: ").strip().lower()

    for p in pokemons_disponiveis:
        if p["nome"].lower() == nome:
            if any(pk["nome"].lower() == nome for pk in pokedex):
                print(f"\nVocê já capturou {p['nome']}.")
                time.sleep(1.5)
                return
            novo_pokemon = {
                "id": str(uuid.uuid4())[:8],
                "nome": p["nome"],
                "tipo": p["tipo"]
            }
            pokedex.append(novo_pokemon)
            salvar_dados()
            print(f"\nVocê capturou {p['nome']}! (ID: {novo_pokemon['id']})")
            time.sleep(1.5)
            return

    print("\nPokémon não encontrado. Verifique o nome digitado.")
    time.sleep(1.5)

# Remover Pokémon
def remover_pokemon():
    if not pokedex:
        print("\nVocê não possui Pokémons capturados.")
        input("\n(Pressione Enter para voltar)")
        return

    print("\nPokémons na sua Pokédex:")
    for p in pokedex:
        print(f"ID: {p['id']} | Nome: {p['nome']} | Tipo: {p['tipo']}")

    id_remover = input("\nDigite o ID do Pokémon que deseja remover: ").strip()
    for p in pokedex:
        if p["id"] == id_remover:
            pokedex.remove(p)
            salvar_dados()
            print(f"\n{p['nome']} foi removido da Pokédex.")
            time.sleep(1.5)
            return

    print("\nID não encontrado na sua Pokédex.")
    time.sleep(1.5)

# Adicionar Pokémon manualmente
def adicionar_pokemon():
    nome = input("\nDigite o nome do novo Pokémon: ").strip().title()
    tipo = input("Digite o tipo do novo Pokémon: ").strip().title()

    if any(p["nome"].lower() == nome.lower() for p in pokemons_disponiveis):
        print("\nEsse Pokémon já está na lista de disponíveis.")
        time.sleep(1.5)
        return

    novo = {"nome": nome, "tipo": tipo}
    pokemons_disponiveis.append(novo)
    salvar_dados()
    print(f"\n{nome} adicionado com sucesso à lista de disponíveis!")
    time.sleep(1.5)

# Sistema principal
def iniciar_pokedex():
    carregar_dados()
    treinador = boas_vindas()
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Olá, {treinador}! Digite 'menu' para abrir o menu da Pokédex a qualquer momento.")

    while True:
        comando = input("\nO que deseja fazer? ")

        if comando.lower() == "menu":
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                exibir_menu()
                opcao = input("\nEscolha uma opção: ")

                if opcao == "1":
                    ver_pokedex()
                elif opcao == "2":
                    capturar_pokemon()
                elif opcao == "3":
                    remover_pokemon()
                elif opcao == "4":
                    adicionar_pokemon()
                elif opcao == "5":
                    print(f"\nAté mais, {treinador}! Boa jornada Pokémon!")
                    salvar_dados()
                    return
                elif opcao.lower() == "menu":
                    break
                else:
                    print("\nOpção inválida!")
                    time.sleep(1.5)
        else:
            print("Digite 'menu' para abrir o menu da Pokédex.")

# Executar o sistema
if __name__ == "__main__":
    iniciar_pokedex()
