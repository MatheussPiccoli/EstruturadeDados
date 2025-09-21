# Alunos: Matheus Pereira e Matheus Piccoli

class Node:
    def __init__(self, dados=None):
        self.__dados = dados
        self.__prev = None
        self.__prox = None

    @property
    def dados(self):
        return self.__dados

    @property
    def prev(self):
        return self.__prev

    @property
    def prox(self):
        return self.__prox

    @dados.setter
    def dados(self, novo_dado):
        self.__dados = novo_dado

    @prev.setter
    def prev(self, novo_no):
        self.__prev = novo_no

    @prox.setter
    def prox(self, novo_no):
        self.__prox = novo_no


class ListaDuplamenteEncadeada:
    def __init__(self, tamanho_maximo):
        self.__header = Node()
        self.__trailer = Node()
        self.__header.prox = self.__trailer
        self.__trailer.prev = self.__header
        self.__cursor = self.__header
        self.__tamanho_maximo = tamanho_maximo
        self.__tamanho = 0

    def __str__(self):
        if self.Vazia():
            return "[]"
        return f"[{self._str_recursivo(self.__header.prox)}]"

    def _str_recursivo(self, no_atual):
        if no_atual == self.__trailer:
            return ""
        if no_atual.prox == self.__trailer:
            return f"{no_atual.dados}"
        return f"{no_atual.dados}, {self._str_recursivo(no_atual.prox)}"

    def Vazia(self):
        return self.__header.prox is self.__trailer

    def Cheia(self):
        return self.__tamanho >= self.__tamanho_maximo
    
    @property
    def tamanho(self):
        return self.__tamanho
    
    @property
    def tamanho_maximo(self):
        return self.__tamanho_maximo

    def _irParaPrimeiro(self):
        if not self.Vazia():
            self.__cursor = self.__header.prox

    def _irParaUltimo(self):
        if not self.Vazia():
            self.__cursor = self.__trailer.prev

    def _avancarKPosicoes(self, k):
        if k < 0:
            raise ValueError("K deve ser um número não-negativo.")
        if k == 0:
            return
        if self.__cursor.prox is self.__trailer:
            raise IndexError("Limite atingido. O cursor está no fim da lista.")
        
        self.__cursor = self.__cursor.prox
        self._avancarKPosicoes(k - 1)

    def _retrocederKPosicoes(self, k):
        if k < 0:
            raise ValueError("K deve ser um número não-negativo.")
        if k == 0:
            return
        if self.__cursor.prev is self.__header:
            raise IndexError("Limite atingido. O cursor está no início da lista.")

        self.__cursor = self.__cursor.prev
        self._retrocederKPosicoes(k - 1)

    def acessarAtual(self):
        if self.__cursor is not self.__header and self.__cursor is not self.__trailer:
            return self.__cursor.dados
        return None

    def inserirAntesDoAtual(self, novo_dado):
        if self.__cursor is self.__header:
            raise IndexError("Não é possível inserir antes do início da lista.")
        elif self.__tamanho >= self.__tamanho_maximo:
            raise Exception("A lista está cheia!")
        
        novo_no = Node(novo_dado)
        no_anterior = self.__cursor.prev
        
        novo_no.prox = self.__cursor
        novo_no.prev = no_anterior
        no_anterior.prox = novo_no
        self.__cursor.prev = novo_no
        
        self.__tamanho += 1

    def inserirAposAtual(self, novo_dado):
        if self.__cursor is self.__trailer:
            raise IndexError("Não é possível inserir após o fim da lista.")
        elif self.__tamanho >= self.__tamanho_maximo:
            raise Exception("A lista está cheia!")

        novo_no = Node(novo_dado)
        proximo_no = self.__cursor.prox
        
        novo_no.prev = self.__cursor
        novo_no.prox = proximo_no
        self.__cursor.prox = novo_no
        proximo_no.prev = novo_no
        
        self.__tamanho += 1

    def inserirComoPrimeiro(self, novo_dado):
        self.__cursor = self.__header
        self.inserirAposAtual(novo_dado)

    def inserirComoUltimo(self, novo_dado):
        self.__cursor = self.__trailer.prev
        if self.Vazia():
            self.__cursor = self.__header
        self.inserirAposAtual(novo_dado)
    
    def inserirNaPosicao(self, k, novo_dado):
        if not (1 <= k <= self.__tamanho + 1):
            raise IndexError("Posição Inválida para inserção.")
        elif self.__tamanho >= self.__tamanho_maximo:
            raise Exception("A lista está cheia!")
        
        self._irParaPrimeiro()
        if k > 1:
          self._avancarKPosicoes(k - 2) 
        
        self.inserirAposAtual(novo_dado)

    def excluirAtual(self):
        if self.__cursor is self.__header or self.__cursor is self.__trailer or self.Vazia():
            raise IndexError("Não é possível excluir. Posição do cursor inválida.")
        
        no_excluir = self.__cursor
        no_anterior = no_excluir.prev
        proximo_no = no_excluir.prox
        
        no_anterior.prox = proximo_no
        proximo_no.prev = no_anterior
        
        self.__cursor = proximo_no
        self.__tamanho -= 1
        return no_excluir.dados

    def excluirPrim(self):
        if self.Vazia():
            raise IndexError("A lista está vazia.")
        self._irParaPrimeiro()
        return self.excluirAtual()

    def excluirUlt(self):
        if self.Vazia():
            raise IndexError("A lista está vazia.")
        self._irParaUltimo()
        return self.excluirAtual()

    def buscar(self, chave):
        return self._buscar_recursivo(self.__header.prox, chave)

    def _buscar_recursivo(self, no_atual, chave):
        if no_atual == self.__trailer:
            return False 
        
        if no_atual.dados == chave:
            self.__cursor = no_atual
            return True
        
        return self._buscar_recursivo(no_atual.prox, chave)

    def posicaoDe(self, chave):
        return self._posicaoDe_recursivo(self.__header.prox, chave, 1)

    def _posicaoDe_recursivo(self, no_atual, chave, pos_atual):
        if no_atual == self.__trailer:
            return -1
        
        if no_atual.dados == chave:
            return pos_atual
        
        return self._posicaoDe_recursivo(no_atual.prox, chave, pos_atual + 1)


if __name__ == "__main__":
    print("--- Iniciando demonstração da Lista Duplamente Encadeada ---")
    
    lista = ListaDuplamenteEncadeada(10) 
    print(f"Lista criada. Está vazia? {lista.Vazia()}. Tamanho: {lista.tamanho}")
    print(f"O tamanho máximo da lista é {lista.tamanho_maximo}")
    print(f"Estado inicial da lista: {lista}\n")
    
    lista.inserirComoPrimeiro(10)
    print(f"Inserindo 10 como primeiro: {lista}")
    lista.inserirComoUltimo(30)
    print(f"Inserindo 30 como último: {lista}")
    lista.buscar(10)
    lista.inserirAposAtual(20)
    print(f"Inserindo 20 após o 10 (via cursor): {lista}")
    lista.inserirNaPosicao(1, 5)
    print(f"Inserindo 5 na posição 1: {lista}")
    print(f"Tamanho atual: {lista.tamanho}")
    print(f"A lista está cheia? {lista.Cheia()}\n")

    chave_busca = 30
    encontrou = lista.buscar(chave_busca)
    print(f"Buscando pelo elemento {chave_busca}... Encontrou? {encontrou}")
    if encontrou:
        print(f"Cursor agora está no elemento: {lista.acessarAtual()}")
    
    pos = lista.posicaoDe(chave_busca)
    print(f"A posição do elemento {chave_busca} é: {pos}\n")

    print(f"Estado da lista antes da exclusão: {lista}")
    removido = lista.excluirUlt()
    print(f"Excluindo o último elemento ({removido}): {lista}")
    removido = lista.excluirPrim()
    print(f"Excluindo o primeiro elemento ({removido}): {lista}")

    print("Buscando pelo elemento 20 para excluir...")
    lista.buscar(20)
    removido = lista.excluirAtual()
    print(f"Excluindo o elemento atual ({removido}): {lista}")

    print("--- Iniciando Teste 2: Lista Cheia ---")
    lista2 = ListaDuplamenteEncadeada(3)
    print(f"Lista2 criada. Tamanho máximo: {lista2.tamanho_maximo}\n")

    try:
        lista2.inserirComoUltimo(1)
        lista2.inserirComoUltimo(2)
        lista2.inserirComoUltimo(3)
        print(f"Lista2 após 3 inserções: {lista2} (Tamanho: {lista2.tamanho})")

        print("Tentando inserir mais um elemento...")
        lista2.inserirComoUltimo(4)

    except Exception as e:
        print(f"Exception: {e}")

    print(f"Estado final da Lista2: {lista2} (Tamanho: {lista2.tamanho})")
    print(f"A lista está cheia? {lista2.Cheia()}")

    print(f"\n--- Fim da demonstração ---")