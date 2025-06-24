
class NoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def obter_altura(self, no):
        if not no:
            return 0
        return no.altura

    def obter_fator_balanceamento(self, no):
        if not no:
            return 0
        return self.obter_altura(no.esquerda) - self.obter_altura(no.direita)

    def atualizar_altura(self, no):
        if no:
            no.altura = 1 + max(self.obter_altura(no.esquerda), self.obter_altura(no.direita))

    def rotacao_direita(self, z):
        y = z.esquerda
        T3 = y.direita

        y.direita = z
        z.esquerda = T3

        self.atualizar_altura(z)
        self.atualizar_altura(y)

        return y

    def rotacao_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda

        y.esquerda = z
        z.direita = T2

        self.atualizar_altura(z)
        self.atualizar_altura(y)

        return y

    def inserir(self, raiz, valor):
        if not raiz:
            return NoAVL(valor)

        if valor < raiz.valor:
            raiz.esquerda = self.inserir(raiz.esquerda, valor)
        elif valor > raiz.valor:
            raiz.direita = self.inserir(raiz.direita, valor)
        else:
            # Valor já existe, não inserir duplicata
            return raiz

        self.atualizar_altura(raiz)

        fator = self.obter_fator_balanceamento(raiz)

        # Caso LL
        if fator > 1 and valor < raiz.esquerda.valor:
            return self.rotacao_direita(raiz)

        # Caso RR
        if fator < -1 and valor > raiz.direita.valor:
            return self.rotacao_esquerda(raiz)

        # Caso LR
        if fator > 1 and valor > raiz.esquerda.valor:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)

        # Caso RL
        if fator < -1 and valor < raiz.direita.valor:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz

    def obter_menor_valor_no(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def remover(self, raiz, valor):
        if not raiz:
            return raiz

        if valor < raiz.valor:
            raiz.esquerda = self.remover(raiz.esquerda, valor)
        elif valor > raiz.valor:
            raiz.direita = self.remover(raiz.direita, valor)
        else:
            if raiz.esquerda is None:
                temp = raiz.direita
                raiz = None
                return temp
            elif raiz.direita is None:
                temp = raiz.esquerda
                raiz = None
                return temp

            temp = self.obter_menor_valor_no(raiz.direita)
            raiz.valor = temp.valor
            raiz.direita = self.remover(raiz.direita, temp.valor)

        if raiz is None:
            return raiz

        self.atualizar_altura(raiz)

        fator = self.obter_fator_balanceamento(raiz)

        # Caso LL
        if fator > 1 and self.obter_fator_balanceamento(raiz.esquerda) >= 0:
            return self.rotacao_direita(raiz)

        # Caso LR
        if fator > 1 and self.obter_fator_balanceamento(raiz.esquerda) < 0:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)

        # Caso RR
        if fator < -1 and self.obter_fator_balanceamento(raiz.direita) <= 0:
            return self.rotacao_esquerda(raiz)

        # Caso RL
        if fator < -1 and self.obter_fator_balanceamento(raiz.direita) > 0:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz

    def pre_ordem(self, no):
        if not no:
            return []
        return [no.valor] + self.pre_ordem(no.esquerda) + self.pre_ordem(no.direita)

    def em_ordem(self, no):
        if not no:
            return []
        return self.em_ordem(no.esquerda) + [no.valor] + self.em_ordem(no.direita)

    def pos_ordem(self, no):
        if not no:
            return []
        return self.pos_ordem(no.esquerda) + self.pos_ordem(no.direita) + [no.valor]


# Exemplo de uso:
avl_tree = ArvoreAVL()
raiz = None

valores_inserir = [10, 20, 30, 40, 50, 25]
print("\n--- Inserção de elementos ---")
for valor in valores_inserir:
    raiz = avl_tree.inserir(raiz, valor)
    print(f"Inserindo {valor}. Árvore em pré-ordem: {avl_tree.pre_ordem(raiz)}")

print("\nÁrvore AVL final (pré-ordem):", avl_tree.pre_ordem(raiz))
print("Árvore AVL final (em ordem):", avl_tree.em_ordem(raiz))

print("\n--- Remoção de elementos ---")
valores_remover = [20, 10]
for valor in valores_remover:
    print(f"Removendo {valor}...")
    raiz = avl_tree.remover(raiz, valor)
    print(f"Árvore em pré-ordem após remoção de {valor}: {avl_tree.pre_ordem(raiz)}")

print("\nÁrvore AVL final após remoções (pré-ordem):", avl_tree.pre_ordem(raiz))
print("Árvore AVL final após remoções (em ordem):", avl_tree.em_ordem(raiz))


