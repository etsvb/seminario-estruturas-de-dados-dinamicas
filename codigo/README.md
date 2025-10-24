# <img src="https://i.pinimg.com/originals/d9/cb/c3/d9cbc37ddc1843e3febf945180f60602.gif" width="40"> Projeto: Pokédex – Estruturas de Dados Dinâmicas em Python

## <img src="https://64.media.tumblr.com/e7ecce28a79842122e6faf8853183708/f72828b12c6f8d7f-b0/s400x600/bf4a0827f4c8edd3cfe27b1612834a2c6ad6e171.gif" width="50"> Descrição do Projeto

Este projeto foi desenvolvido para demonstrar **o uso de estruturas de dados dinâmicas** em Python, aplicadas de forma prática e divertida por meio de uma **Pokédex interativa** inspirada no universo Pokémon.  

A aplicação permite ao usuário iniciar uma jornada Pokémon, capturar, visualizar, remover e cadastrar manualmente novos Pokémons, utilizando conceitos fundamentais de **listas dinâmicas, objetos e manipulação de dados em tempo de execução**.

---

## <img src="https://i.pinimg.com/originals/3c/06/59/3c06599306cca1e170ce8df10949cf91.gif" width="40"> Objetivos de Aprendizado

O objetivo do projeto é aplicar conceitos de **Estruturas de Dados Dinâmicas**, como:

- **Listas dinâmicas (`list`)** — usadas para armazenar e manipular Pokémons capturados ou disponíveis.
- **Objetos e classes** — para representar cada Pokémon com atributos e comportamentos.
- **IDs únicos** — gerados dinamicamente no momento da captura, simulando um sistema de identificação.
- **Remoção e inserção de elementos** — exemplificando operações comuns em estruturas dinâmicas.

---

## <img src="https://64.media.tumblr.com/66ebd74acd32a3fd62c26aad77026d0c/130cb53d5c4bca5c-9a/s250x400/63a287d5a2e1b9a8358ba4c683ad3c98f9145214.gif" width="50"> Funcionalidades

### Boas-vindas e Jornada
- Ao iniciar o programa, o usuário é recebido com uma mensagem de boas-vindas.
- O jogador informa seu nome e inicia sua jornada Pokémon.

### Sistema de Menu Interativo
- O menu **só é exibido quando o jogador o chama**, criando uma experiência mais imersiva.
- O usuário pode navegar entre as opções pressionando ENTER para retornar ao menu.

### Pokédex (Lista Dinâmica)
- Exibe todos os Pokémons cadastrados no jogo.
- Mostra se o Pokémon está **“CAPTURADO”** ou **“BLOQUEADO”** (ainda não capturado).
- A lista é atualizada em tempo real conforme as capturas e remoções são feitas.

| Nome       | Tipo      | Gif             |
|------------|-----------|-----------------|
| Bulbasaur  | Planta    |<img src="https://i.pinimg.com/originals/e5/35/ad/e535ad30166d0121722774e0275bef3f.gif" width="80"> |
| Charmander | Fogo      |<img src="https://i.pinimg.com/originals/48/1e/af/481eafa3a380198012f80595c0dafeec.gif" width="50"> |
| Pikachu    | Elétrico  |<img src="https://i.pinimg.com/originals/a7/a8/d0/a7a8d06c754cfbbbc37e64cb118c513c.gif" width="50"> |

### 4. Captura de Pokémons
- O jogador pode capturar um Pokémon digitando seu nome.
- Cada captura gera um **ID único** (usando o módulo `uuid`).
- Se o Pokémon já estiver capturado, o sistema avisa o usuário.

###  Remoção de Pokémons
- O jogador pode remover um Pokémon da Box digitando seu ID.
- A Box é atualizada dinamicamente, removendo o item da lista.

### Adicionar Pokémon Manualmente
- Permite ao jogador adicionar novos Pokémons à Pokédex.
- Se o Pokémon já existir, o sistema impede duplicação.

---

## <img src="https://i.pinimg.com/originals/46/04/8d/46048da1b8533b654955f33e5cf40438.gif" width="80"> Estruturas de Dados Utilizadas

| Estrutura | Tipo | Descrição |
|------------|------|-----------|
| `list` | Dinâmica | Armazena os Pokémons capturados e os disponíveis. |
| `class Pokemon` | Objeto | Representa um Pokémon com nome e ID. |
| `class Pokedex` | Objeto | Gerencia as listas, capturas, remoções e exibições. |
| `uuid.uuid4()` | Função | Gera IDs únicos para cada Pokémon capturado. |

---

## <img src="https://64.media.tumblr.com/65860273016c3b7089dacd1728b1464c/9c78cd16d5cd77b4-bf/s250x400/74ac58099061fc2e6bec3c84c3d45da63f2af503.gif" width="80"> Como Utilizar

##  Requisitos <img src="https://64.media.tumblr.com/b19aa6cdcf1fb672fb4e7333eb994573/31c486a7eb1b7a6c-f9/s500x750/943d2fe64e5392fa33efa7f90b5d9425e81c2bc6.gif" width="500">

- **Python 3.7+** ![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)

### 1. Executar o programa
No terminal, execute:

```bash
python pokedex.py
```

### 2. Iniciar a jornada
Digite seu nome e pressione ENTER.

### 3. Acessar o menu principal
Após o início, pressione ENTER sempre que desejar abrir o menu.

### 4. Opções disponíveis no menu

| Opção | Ação |
|--------|-------|
| 1 | Mostrar Pokédex (com status de captura) |
| 2 | Capturar Pokémon pelo nome |
| 3 | Mostrar Box com Pokémons capturados |
| 4 | Remover Pokémon pelo ID |
| 5 | Adicionar Pokémon manualmente |
| 6 | Encerrar o programa |

---

##  <img src="https://64.media.tumblr.com/3264f5d7743d8d14c3c6e86059a2ea99/95959a0f994cf4df-81/s250x400/ee7078065a83726a2f9d94936c5452d47356c8c8.gif" width="40"> Exemplo de Execução

```
Bem-vindo ao mundo Pokémon!
Digite seu nome para iniciar a jornada: Ericha
Olá, Ericha! Sua jornada Pokémon começa agora.

Pressione ENTER para abrir o menu e começar sua aventura...

=== MENU ===
1. Mostrar Pokédex
2. Capturar Pokémon
3. Mostrar Box
4. Remover Pokémon da Box
5. Adicionar Pokémon Manualmente
6. Sair
Escolha uma opção: 2

Digite o nome do Pokémon que deseja capturar: Pikachu
Pikachu foi capturado! ID: a3f9c2d1
```

---

## <img src="https://64.media.tumblr.com/ad55d6ddcd8d5429cbeacd2b1e977b33/1d9199f2cdd51f15-17/s100x200/7f3302eb2b742d5a4da22678fe614909f0113fb8.gif" width="40"> Estrutura de Arquivos

```
 pokedex/
│
├── pokedex.py        # Código principal do projeto
└── README.md          # Documentação do projeto (este arquivo)
```

---

## Conceitos Demonstrados

- **Encapsulamento e Classes**
- **Listas dinâmicas e manipulação de elementos**
- **Geração e controle de IDs**
- **Menus interativos e loops**
- **Boas práticas de programação em Python**

---

## Autor

Desenvolvido por **Ericha T. S. Barbosa**  
Trabalho acadêmico sobre **Estruturas de Dados Dinâmicas** em Python.

---

##  Licença

Este projeto é livre para fins educacionais e de aprendizado.  
