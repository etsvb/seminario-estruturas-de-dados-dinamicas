# Pokédex PyQt

Uma aplicação gráfica simples feita com **PyQt5** que simula uma
**Pokédex interativa**, permitindo capturar, visualizar, adicionar e
remover Pokémon.
Os dados são salvos localmente em arquivos `.json`, garantindo que suas
capturas sejam mantidas entre sessões.

---

## Funcionalidades

-    **Ver Pokédex** -- mostra todos os Pokémon disponíveis e indica
    quais já foram capturados.
-    **Capturar Pokémon** -- escolha um Pokémon disponível para
    adicioná-lo à sua Pokédex.
-    **Remover Pokémon** -- remova um Pokémon capturado através do seu
    ID único.
-    **Adicionar Pokémon** -- adicione novos Pokémon à lista de
    disponíveis.
-    **Salvar e Sair** -- salva automaticamente todos os dados antes
    de fechar a aplicação.

---

##  Tecnologias utilizadas

-   **Python 3.8+**
-   **PyQt5** -- para a interface gráfica
-   **JSON** -- para salvar os dados localmente

------------------------------------------------------------------------

##  Estrutura de arquivos

     projeto_pokedex/
    │
    ├── pokedexPyQt.py                # Código principal da aplicação
    ├── pokedex.json                  # Lista dos Pokémon capturados (gerado automaticamente)
    ├── pokemons_disponiveis.json     # Lista dos Pokémon disponíveis (gerado automaticamente)
    └── README.md                     # Documentação do projeto

------------------------------------------------------------------------

##  Como rodar na sua máquina

### 1️ Instalar o Python

Baixe e instale o Python no site oficial:
 <https://www.python.org/downloads/>\
Durante a instalação, **marque a opção "Add Python to PATH"**.

------------------------------------------------------------------------

###  Instalar dependências

Abra o terminal (ou prompt de comando) e rode:

``` bash
pip install pyqt5
```

------------------------------------------------------------------------

###  Baixar o projeto

Você pode: - Clonar o repositório:
`bash   git clone https://github.com/seuusuario/pokedexPyQt.git   cd pokedexPyQt` 

Ou baixar o arquivo `pokedexPyQt.py` diretamente.

------------------------------------------------------------------------

### Executar o programa

No terminal, dentro da pasta do projeto, execute:

``` bash
python pokedexPyQt.py
```

A janela da Pokédex será aberta com os botões: 
- **Ver Pokédex**
- **Capturar Pokémon**
- **Remover Pokémon**
- **Adicionar Pokémon** ]
- **Salvar e Sair**

------------------------------------------------------------------------

## Persistência dos dados

Os arquivos `pokedex.json` e `pokemons_disponiveis.json` são criados
automaticamente no primeiro uso.
Eles armazenam as informações de captura e da lista de Pokémon
disponíveis.

-   `pokedex.json` → guarda os Pokémon capturados.
-   `pokemons_disponiveis.json` → guarda todos os Pokémon possíveis de
    capturar.

------------------------------------------------------------------------

## Dica

Se quiser **recomeçar do zero**, basta apagar os arquivos `pokedex.json`
e `pokemons_disponiveis.json`.
Na próxima execução, eles serão recriados com a lista padrão (Pikachu,
Charmander, Bulbasaur, etc).

------------------------------------------------------------------------

##  Autor

Desenvolvido por **Ericha T. S. Barbosa** 

Licença: MIT(https://opensource.org/licenses/MIT)
