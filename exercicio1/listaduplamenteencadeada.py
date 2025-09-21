class Node:
  def __init__(self, dados=None):
    self.__dados = dados
    self.__prev = None
    self.__prox = None

class ListaDuplamenteEncadeada:
  def __init__(self, tamanho):
    self.__header = Node()
    self.__trailer = Node()
    self.__header.prox = self.__trailer
    self.__trailer.prev = self.__header
    self.__cursor = self.header
    self.__tamanho = tamanho

  def Vazia(self):
    return self.__header.prox is self.__trailer
  
  def Cheia(self):
    return False
  
  def IrParaPrimeiro(self):
    self.__cursor = self.__header.prox

  def IrParaUltimo(self):
    self.__cursor = self.__trailer.prev

  def AvancarKPosicoes(self, k):
    contador = 0
    while contador < k:
      if self.__cursor.prox is not self.__trailer:
        self.__cursor = self.__cursor.prox
      else:
        raise Exception("Limite atingido. O cursor está no fim da lista")
  
  def RetrocederKPosicoes(self, k):
    contador = 0
    while contador < k:
      if self.__cursor.prev is not self.__header:
        self.__cursor = self.__cursor.prev
      else:
        raise Exception("Limite atingido. O cursor está no início da lista")
      
  def AcessarAtual(self):
    if self.__cursor is not self.__header and self.__cursor is not self.__trailer:
      return self.__cursor.dado
    return None
  
  def InserirAntesdoAtual(self, novo_dado):
    if self.__cursor is self.__header:
      self.__cursor = self.__header.prox

    novo_no = Node(novo_dado)
    no_anterior = self.__cursor.prev
     
    novo_no.prox = self.__cursor
    novo_no.anterior = no_anterior

    no_anterior.prox = novo_no
    self.__cursor.prev = novo_no

    self.__tamanho += 1

  def InserirAposAtual(self, novo_dado):
    if self.__cursor is self.__trailer:
      self.__cursor = self.__trailer.prev

    novo_no = Node(novo_dado)
    proximo_no = self.__cursor.prox

    novo_no.prev = self.__cursor
    novo_no.prox = proximo_no

    self.__cursor.prox = novo_no
    proximo_no.anterior = novo_no
    
    self.__tamanho += 1

  def InserirComoPrimeiro(self, novo_dado):
    self.__cursor = self.__header
    self.InserirAposAtual(novo_dado)

  def InserirComoUltimo(self, novo_dado):
    self.__cursor = self.__trailer
    self.InserirAntesdoAtual(novo_dado)

  def InserirNaPosicao(self, k, novo_dado):
    if k < 0 or k > self.__tamanho:
      raise Exception("Posicção Invalida")
    
    self.IrParaPrimeiro
    self.AvancarKPosicoes(k)
    self.InserirAntesdoAtual(novo_dado)

  def ExcluirAtual(self):
    if self.__cursor is self.__trailer or self.__cursor is self.__header:
      raise Exception("Não é possível excluir o trailer/header")
    
    no_excluir = self.__cursor

    no_excluir.prev.prox = no_excluir.prox
    no_excluir.prox.prev = no_excluir.prev
    self.__cursor = no_excluir.prox

    self.__tamanho -= 1

  def ExcluirPrimeiro(self):
    if not self.Vazia():
      self.IrParaPrimeiro()
      self.ExcluirAtual()

  def ExcluirUltimo(self):
    if not self.Vazia():
      self.IrParaUltimo()
      self.ExcluirAtual()

  def Buscar(self, chave):
    return