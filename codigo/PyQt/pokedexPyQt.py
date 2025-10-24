import sys
import os
import json
import uuid
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, 
    QMessageBox, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, 
    QHBoxLayout, QInputDialog
)
from PyQt5.QtCore import Qt

ARQUIVO_POKEDEX = "pokedex.json"
ARQUIVO_POKEMONS = "pokemons_disponiveis.json"

# Funções de persistência
def salvar_dados(pokedex, pokemons_disponiveis):
    with open(ARQUIVO_POKEDEX, "w", encoding="utf-8") as f:
        json.dump(pokedex, f, indent=4, ensure_ascii=False)
    with open(ARQUIVO_POKEMONS, "w", encoding="utf-8") as f:
        json.dump(pokemons_disponiveis, f, indent=4, ensure_ascii=False)

def carregar_dados():
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
    return pokedex, pokemons_disponiveis

# Interface principal
class PokedexApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokédex PyQt")
        self.resize(600, 400)

        self.pokedex, self.pokemons_disponiveis = carregar_dados()

        # Layout principal
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(3)
        self.tabela.setHorizontalHeaderLabels(["ID", "Nome", "Tipo"])
        main_layout.addWidget(self.tabela)

        # Botões
        btn_ver = QPushButton("Ver Pokédex")
        btn_capturar = QPushButton("Capturar Pokémon")
        btn_remover = QPushButton("Remover Pokémon")
        btn_adicionar = QPushButton("Adicionar Pokémon")
        btn_sair = QPushButton("Salvar e Sair")

        for b in [btn_ver, btn_capturar, btn_remover, btn_adicionar, btn_sair]:
            main_layout.addWidget(b)

        # Ações
        btn_ver.clicked.connect(self.ver_pokedex)
        btn_capturar.clicked.connect(self.capturar_pokemon)
        btn_remover.clicked.connect(self.remover_pokemon)
        btn_adicionar.clicked.connect(self.adicionar_pokemon)
        btn_sair.clicked.connect(self.fechar_app)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        self.ver_pokedex()

    # Funções principais
    def ver_pokedex(self):
        self.tabela.setRowCount(0)
        for p in self.pokemons_disponiveis:
            capturado = next((pk for pk in self.pokedex if pk["nome"].lower() == p["nome"].lower()), None)
            row = self.tabela.rowCount()
            self.tabela.insertRow(row)
            if capturado:
                self.tabela.setItem(row, 0, QTableWidgetItem(capturado["id"]))
                self.tabela.setItem(row, 1, QTableWidgetItem(p["nome"]))
                self.tabela.setItem(row, 2, QTableWidgetItem(p["tipo"]))
            else:
                self.tabela.setItem(row, 0, QTableWidgetItem("—"))
                self.tabela.setItem(row, 1, QTableWidgetItem(p["nome"] + " (bloqueado)"))
                self.tabela.setItem(row, 2, QTableWidgetItem(p["tipo"]))

    def capturar_pokemon(self):
        nomes = [p["nome"] for p in self.pokemons_disponiveis]
        nome, ok = QInputDialog.getItem(self, "Capturar Pokémon", "Escolha o Pokémon:", nomes, 0, False)
        if ok and nome:
            if any(pk["nome"].lower() == nome.lower() for pk in self.pokedex):
                QMessageBox.information(self, "Info", f"Você já capturou {nome}!")
                return
            p = next(p for p in self.pokemons_disponiveis if p["nome"] == nome)
            novo_pokemon = {
                "id": str(uuid.uuid4())[:8],
                "nome": p["nome"],
                "tipo": p["tipo"]
            }
            self.pokedex.append(novo_pokemon)
            salvar_dados(self.pokedex, self.pokemons_disponiveis)
            QMessageBox.information(self, "Sucesso", f"{p['nome']} capturado com sucesso!")
            self.ver_pokedex()

    def remover_pokemon(self):
        if not self.pokedex:
            QMessageBox.warning(self, "Aviso", "Você não tem nenhum Pokémon capturado.")
            return
        ids = [p["id"] for p in self.pokedex]
        id_escolhido, ok = QInputDialog.getItem(self, "Remover Pokémon", "Escolha o ID para remover:", ids, 0, False)
        if ok and id_escolhido:
            self.pokedex = [p for p in self.pokedex if p["id"] != id_escolhido]
            salvar_dados(self.pokedex, self.pokemons_disponiveis)
            QMessageBox.information(self, "Removido", f"Pokémon removido com sucesso!")
            self.ver_pokedex()

    def adicionar_pokemon(self):
        nome, ok1 = QInputDialog.getText(self, "Adicionar Pokémon", "Nome do Pokémon:")
        if not ok1 or not nome.strip():
            return
        tipo, ok2 = QInputDialog.getText(self, "Adicionar Pokémon", "Tipo do Pokémon:")
        if not ok2 or not tipo.strip():
            return
        if any(p["nome"].lower() == nome.lower() for p in self.pokemons_disponiveis):
            QMessageBox.warning(self, "Erro", "Esse Pokémon já existe na lista!")
            return
        novo = {"nome": nome.title(), "tipo": tipo.title()}
        self.pokemons_disponiveis.append(novo)
        salvar_dados(self.pokedex, self.pokemons_disponiveis)
        QMessageBox.information(self, "Sucesso", f"{nome.title()} adicionado com sucesso!")
        self.ver_pokedex()

    def fechar_app(self):
        salvar_dados(self.pokedex, self.pokemons_disponiveis)
        QMessageBox.information(self, "Saída", "Dados salvos com sucesso. Até mais, treinador!")
        self.close()

# Executar
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = PokedexApp()
    janela.show()
    sys.exit(app.exec_())
