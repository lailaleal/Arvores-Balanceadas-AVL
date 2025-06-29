# Arvores-Balanceadas-AVL
Seminário de Estrutura de Dados 2

![Captura de tela 2025-06-29 192707](https://github.com/user-attachments/assets/55d7636b-4d23-4299-9c95-b4948d8da077)

Uma Árvore AVL é uma Árvore Binária de Busca (ABB) auto-balanceada. Isso significa que, para qualquer nó na árvore, a diferença de altura entre suas subárvores esquerda e direita (conhecida como fator de balanceamento) nunca é maior que . Essa propriedade garante que a altura da árvore seja sempre logarítmica em relação ao número de nós, o que resulta em operações de busca, inserção e remoção com complexidade de tempo O(log n) no pior caso.

![Captura de tela 2025-06-29 192730](https://github.com/user-attachments/assets/3771f96f-c51d-424a-b1b5-3931e9a0cc9a)

## Fator de Balanceamento

O fator de balanceamento de um nó é a altura da sua subárvore esquerda menos a altura da sua subárvore direita. Para uma árvore AVL, o fator de balanceamento de qualquer nó deve ser -,  ou .

Fator de Balanceamento = 0: A altura da subárvore esquerda é igual à altura da subárvore direita.
Fator de Balanceamento = 1: A altura da subárvore esquerda é um a mais que a altura da subárvore direita.
Fator de Balanceamento = -1: A altura da subárvore direita é um a mais que a altura da subárvore esquerda.

![Captura de tela 2025-06-29 192803](https://github.com/user-attachments/assets/176df188-6cb3-4271-a854-37c31f2b3dab)

Se o fator de balanceamento de um nó se torna diferente de -1, 0 ou 1 após uma inserção ou remoção, a árvore está desbalanceada e precisa ser rebalanceada através de rotações.

## Rotações

As rotações são operações que reestruturam a árvore para restaurar a propriedade de balanceamento AVL, sem violar a propriedade da Árvore Binária de Busca. Existem quatro tipos de rotações:

## Rotação Simples à Direita (LL - Left-Left): Ocorre quando um nó é inserido na subárvore esquerda do filho esquerdo de um nó desbalanceado.
![Captura de tela 2025-06-29 192817](https://github.com/user-attachments/assets/8c1382a3-6485-495b-ac50-98204fcdd992)

## Rotação Simples à Esquerda (RR - Right-Right): Ocorre quando um nó é inserido na subárvore direita do filho direito de um nó desbalanceado.
![Captura de tela 2025-06-29 192832](https://github.com/user-attachments/assets/8a1c1199-3e74-41bd-a263-ba852ad64161)


## Rotação Dupla Esquerda-Direita (LR - Left-Right): Ocorre quando um nó é inserido na subárvore direita do filho esquerdo de um nó desbalanceado.
![Captura de tela 2025-06-29 192850](https://github.com/user-attachments/assets/00b5f8c5-b5cd-4236-8566-da37b8e7baa7)

## Rotação Dupla Direita-Esquerda (RL - Right-Left): Ocorre quando um nó é inserido na subárvore esquerda do filho direito de um nó desbalanceado.
![Captura de tela 2025-06-29 192902](https://github.com/user-attachments/assets/2ebe315e-0126-42d3-84f9-fa5e764c5f00)


## Operações

Inserção: A inserção em uma árvore AVL é semelhante à inserção em uma ABB. Após a inserção de um novo nó, é necessário verificar e, se necessário, rebalancear a árvore usando rotações, começando do nó inserido e subindo até a raiz.
Remoção: A remoção em uma árvore AVL também é semelhante à remoção em uma ABB. Após a remoção de um nó, é necessário verificar e, se necessário, rebalancear a árvore usando rotações, começando do nó removido (ou seu sucessor/antecessor) e subindo até a raiz.
