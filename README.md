# Estruturas de Dados Dinâmicas

> Documentação desenvolvida com base em um estudo sobre **estruturas de
> dados dinâmicas**, abordando conceitos, tipos, implementações em
> Python e aplicações práticas.

------------------------------------------------------------------------

## Introdução

Uma **estrutura de dados** é uma forma organizada de armazenar e
manipular informações em memória.
As **estruturas dinâmicas** se diferenciam das estáticas porque **podem
crescer e diminuir** conforme a necessidade do programa, sem um tamanho
fixo definido.

**Analogia:**
Imagine uma gaveta elástica --- ela se adapta à quantidade de roupas que
você quer guardar.
Na computação, estruturas como listas encadeadas, filas e árvores
funcionam da mesma forma.

------------------------------------------------------------------------

## O que são Estruturas de Dados Dinâmicas ?

São estruturas que **alocam e liberam memória durante a execução do
programa**, permitindo lidar com quantidades variáveis de dados.

**Características principais:** - Tamanho variável; - Alocação de
memória sob demanda; - Uso eficiente da RAM; - Mais flexíveis que
vetores e arrays.

------------------------------------------------------------------------

## Principais Estruturas

###  Listas Encadeadas

Uma **lista encadeada** é uma coleção de nós, onde cada nó contém: - Um
**valor** (dado armazenado); - Um **ponteiro** para o próximo nó (ou
anterior, em listas duplas).

#### Tipos:

-   **Simples** -- cada nó aponta apenas para o próximo;
-   **Dupla** -- nós apontam para o anterior e o próximo;
-   **Circular** -- o último nó aponta para o primeiro.

####  Vantagens:

-   Inserção e remoção rápidas (O(1) em muitos casos);
-   Crescem dinamicamente sem realocação de memória.

####  Desvantagens:

-   Acesso sequencial (O(n) para encontrar um elemento);
-   Risco de "nós perdidos" se ponteiros forem mal configurados.

------------------------------------------------------------------------

###  Filas (Queues)

Uma **fila** segue o princípio **FIFO (First In, First Out)**.
O primeiro elemento a entrar é o primeiro a sair.

#### Operações:

-   `enqueue()` → insere no final
-   `dequeue()` → remove do início
-   `peek()` → visualiza o início sem remover
-   `is_empty()` → verifica se está vazia

#### Tipos:

-   Fila simples
-   Fila circular
-   Deque (fila dupla)

####  Exemplos reais:

-   Fila de impressão (spooler)
-   Fila de processos em sistemas operacionais
-   Buffer de rede
-   Simulações (supermercado, banco, etc.)

------------------------------------------------------------------------

###  Pilhas (Stacks)

Segue o princípio **LIFO (Last In, First Out)**.
O último elemento inserido é o primeiro a ser removido.

#### Operações:

-   `push()` → empilha elemento
-   `pop()` → remove o topo
-   `peek()` → vê o topo sem remover

#### Aplicações:

-   Chamadas de função (recursão);
-   Sistema de undo/redo;
-   Avaliação de expressões matemáticas;
-   Navegação em páginas (voltar/avançar).

------------------------------------------------------------------------

###  Árvores

Estrutura **hierárquica e não linear** composta por nós e arestas.

#### Tipos principais:

-   **Árvore Binária** -- até dois filhos por nó;
-   **Árvore Binária de Busca (BST)** -- mantém a ordem (valores menores
    à esquerda);
-   **Árvore AVL** -- balanceada, garantindo eficiência em
    busca/inserção;
-   **Árvore B / B+** -- usada em bancos de dados e sistemas de
    arquivos.

####  Aplicações:

-   Organização de diretórios;
-   Árvores sintáticas em compiladores;
-   Árvores de decisão em IA e jogos;
-   Índices de bancos de dados.

------------------------------------------------------------------------

##  Exemplos Práticos em Python

### Lista Encadeada Simples

``` python
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, valor):
        novo = Node(valor)
        novo.next = self.head
        self.head = novo

    def display(self):
        atual = self.head
        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.next
        print("None")
```

------------------------------------------------------------------------

### Fila com `collections.deque`

``` python
from collections import deque

fila = deque()
fila.append("Tarefa 1")
fila.append("Tarefa 2")
print(fila.popleft())  # Remove o primeiro elemento
```

------------------------------------------------------------------------

### Pilha com Lista

``` python
pilha = []
pilha.append(10)
pilha.append(20)
print(pilha.pop())  # 20
```

------------------------------------------------------------------------

### Árvore Binária de Busca (BST)

``` python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
```

------------------------------------------------------------------------

##  Aplicações no Mundo Real

-   **Sistemas operacionais** → gerenciamento de processos (filas
    circulares)
-   **Bancos de dados** → árvores B e B+
-   **Redes sociais** → grafos para conexões
-   **Jogos e IA** → árvores de decisão e pilhas para backtracking\
-   **Compiladores** → pilhas e árvores sintáticas

------------------------------------------------------------------------

##  Contribuição

Sinta-se à vontade para abrir **issues** e enviar **pull requests**
com: - Implementações em outras linguagens (C, Java, etc.);
- Melhorias de desempenho;
- Exemplos de aplicações reais.

------------------------------------------------------------------------

## Licença

Este projeto está sob a licença MIT.
Você pode usar, modificar e distribuir o conteúdo livremente, desde que mantenha os créditos.

---

## Fontes:

Estrutura de dados-

- https://www.alura.com.br/artigos/estruturas-de-dados-introducao

Estrutura de Dados.PDF FACOM

Prof. Flávio de Oliveira Silva, M.Sc.

- https://medium.com/@pedro.vaf/estruturas-de-dados-est%C3%A1ticas-vs-estruturas-de-dados-din%C3%A2micas-e92e1d29b8f5

Listas-

- https://www.ime.usp.br/~pf/algoritmos/aulas/lista.html

- https://www.facom.ufu.br/~anilton/EQQ09_PD_EngQuimica/lista_encadeada.pdf

- https://medium.com/@emersoneduardo.airesnunes/listas-encadeadas-utilizando-python-7526f982b4ae

- https://www.youtube.com/watch?v=OwiHoj-mAi8

Filas-

- https://en.wikipedia.org/wiki/Queue_%28abstract_data_type "Queue (abstract data type)"

- https://realpython.com/python-deque "Python's deque: Implement Efficient Queues and Stacks"

- https://www.geeksforgeeks.org/circular-queue-in-python "Circular Queue in Python | GeeksforGeeks"

- https://www.geeksforgeeks.org/introduction-to-circular-queue "Circular Array Implementation of Queue - GeeksforGeeks"

- https://www.programiz.com/dsa/circular-queue "Circular Queue Data Structure - Programiz"

- https://www.ime.usp.br/~pf/algoritmos/aulas/fila.html "O que é uma filas FIFO e como implementá-la eficientemente"

- https://pt.wikipedia.org/wiki/Deque_%28estruturas_de_dados%29 "Deque (estruturas de dados)"

- https://www.algorithmroom.com/dsa/types-of-queues "Types of Queues - Algorithm Room"

- https://www.cos.ufrj.br/~rfarias/cos121/filas.html "Estrutura de Dados e Algoritmos"

Pilhas-

- https://pt.wikipedia.org/wiki/Pilha_(inform%C3%A1tica)

- https://docs.python.org/pt-br/3/library/collections.html?utm_source=

- https://www.cos.ufrj.br/~rfarias/cos121/pilhas.html?utm_source=

- https://www.inf.unioeste.br/~adair/ED/Notas%20de%20Aula/Aulas%20Estruturas%20de%20Dados.pdf?utm_source=

---
Grupo:

- Ericha T. S. Barbosa
- Guilherme Henrique
- Gabriel Tenório
- Danilo Silva
- Marlon Alves
- José Luis
