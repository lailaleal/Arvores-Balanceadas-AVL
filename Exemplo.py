#!/usr/bin/env python3
"""
Exemplos de uso da Árvore AVL
Este arquivo demonstra como usar a implementação da Árvore AVL
"""

from Arvore_AVL import ArvoreAVL, NoAVL

def exemplo_basico():
    """Exemplo básico de inserção e busca"""
    print("=== Exemplo Básico ===")
    
    avl = ArvoreAVL()
    raiz = None
    
    # Inserir alguns valores
    valores = [50, 30, 70, 20, 40, 60, 80]
    print(f"Inserindo valores: {valores}")
    
    for valor in valores:
        raiz = avl.inserir(raiz, valor)
        print(f"Inserido {valor}. Árvore em ordem: {avl.em_ordem(raiz)}")
    
    print(f"\nÁrvore final em ordem: {avl.em_ordem(raiz)}")
    print(f"Árvore final em pré-ordem: {avl.pre_ordem(raiz)}")
    print(f"Altura da árvore: {avl.obter_altura(raiz)}")

def exemplo_rotacoes():
    """Exemplo que demonstra as rotações"""
    print("\n=== Exemplo de Rotações ===")
    
    avl = ArvoreAVL()
    raiz = None
    
    # Caso que força rotação LL (inserção sequencial crescente)
    print("Inserindo 10, 20, 30 (força rotação RR):")
    for valor in [10, 20, 30]:
        raiz = avl.inserir(raiz, valor)
        print(f"Inserido {valor}. Árvore: {avl.pre_ordem(raiz)}")
    
    # Caso que força rotação LR
    print("\nInserindo 40, 50, 45 (força rotação RL):")
    for valor in [40, 50, 45]:
        raiz = avl.inserir(raiz, valor)
        print(f"Inserido {valor}. Árvore: {avl.pre_ordem(raiz)}")

def exemplo_remocao():
    """Exemplo de remoção de elementos"""
    print("\n=== Exemplo de Remoção ===")
    
    avl = ArvoreAVL()
    raiz = None
    
    # Construir uma árvore
    valores = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
    for valor in valores:
        raiz = avl.inserir(raiz, valor)
    
    print(f"Árvore inicial: {avl.em_ordem(raiz)}")
    
    # Remover diferentes tipos de nós
    elementos_remover = [10, 30, 50]  # folha, nó com filhos, raiz
    
    for elemento in elementos_remover:
        print(f"\nRemovendo {elemento}...")
        raiz = avl.remover(raiz, elemento)
        print(f"Árvore após remoção: {avl.em_ordem(raiz)}")
        print(f"Pré-ordem: {avl.pre_ordem(raiz)}")

def exemplo_performance():
    """Exemplo de performance com muitos elementos"""
    print("\n=== Exemplo de Performance ===")
    
    import time
    import random
    
    avl = ArvoreAVL()
    raiz = None
    
    # Gerar números aleatórios
    numeros = list(range(1, 1001))
    random.shuffle(numeros)
    
    print("Inserindo 1000 elementos aleatórios...")
    inicio = time.time()
    
    for numero in numeros:
        raiz = avl.inserir(raiz, numero)
    
    fim = time.time()
    
    print(f"Tempo de inserção: {fim - inicio:.4f} segundos")
    print(f"Altura da árvore: {avl.obter_altura(raiz)}")
    print(f"Altura teórica mínima: {int(__import__('math').log2(1000))}")
    
    # Teste de busca
    elementos_buscar = random.sample(numeros, 100)
    
    inicio = time.time()
    encontrados = 0
    for elemento in elementos_buscar:
        if buscar_elemento(raiz, elemento):
            encontrados += 1
    fim = time.time()
    
    print(f"Tempo de busca (100 elementos): {fim - inicio:.4f} segundos")
    print(f"Elementos encontrados: {encontrados}/100")

def buscar_elemento(raiz, valor):
    """Função auxiliar para buscar um elemento"""
    if not raiz:
        return False
    
    if valor == raiz.valor:
        return True
    elif valor < raiz.valor:
        return buscar_elemento(raiz.esquerda, valor)
    else:
        return buscar_elemento(raiz.direita, valor)

def exemplo_validacao():
    """Exemplo de validação da propriedade AVL"""
    print("\n=== Exemplo de Validação ===")
    
    avl = ArvoreAVL()
    raiz = None
    
    # Inserir elementos
    valores = [100, 50, 150, 25, 75, 125, 175]
    for valor in valores:
        raiz = avl.inserir(raiz, valor)
    
    print(f"Árvore: {avl.em_ordem(raiz)}")
    
    # Verificar propriedade AVL
    def verificar_avl(no):
        if not no:
            return True, 0
        
        esq_valida, altura_esq = verificar_avl(no.esquerda)
        dir_valida, altura_dir = verificar_avl(no.direita)
        
        altura_atual = max(altura_esq, altura_dir) + 1
        fator_balanceamento = altura_esq - altura_dir
        
        valida = (esq_valida and dir_valida and 
                 abs(fator_balanceamento) <= 1)
        
        print(f"Nó {no.valor}: FB = {fator_balanceamento}, Altura = {altura_atual}")
        
        return valida, altura_atual
    
    valida, altura = verificar_avl(raiz)
    print(f"\nÁrvore é AVL válida: {valida}")
    print(f"Altura calculada: {altura}")

def main():
    """Função principal que executa todos os exemplos"""
    print("Demonstração da Árvore AVL")
    print("=" * 50)
    
    exemplo_basico()
    exemplo_rotacoes()
    exemplo_remocao()
    exemplo_performance()
    exemplo_validacao()
    
    print("\n" + "=" * 50)
    print("Demonstração concluída!")

if __name__ == "__main__":
    main()

