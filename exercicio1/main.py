from listaduplamenteencadeada import ListaDuplamenteEncadeada

def teste1():
    print("Teste 1")
    
    lista = ListaDuplamenteEncadeada(10)
    print(f"Lista criada. Está vazia? {lista.Vazia()}. "
          f"Tamanho: {lista.tamanho}. Tamanho máximo: {lista.tamanho_maximo}")
    print(f"Estado inicial da lista: {lista}\n")
    
    lista.inserirComoPrimeiro(10)
    print(f"Inserindo 10 como primeiro: {lista}")
    lista.inserirComoUltimo(30)
    print(f"Inserindo 30 como último: {lista}")
    lista.buscar(10)
    lista.inserirAposAtual(20)
    print(f"Inserindo 20 após o 10: {lista}")
    lista.inserirNaPosicao(1, 5)
    print(f"Inserindo 5 na posição 1: {lista}")
    print(f"Tamanho atual: {lista.tamanho}")
    print(f"A lista está cheia? {lista.Cheia()}\n")

    print(f"Estado da lista antes da exclusão: {lista}")
    removido = lista.excluirUlt()
    print(f"Excluindo último elemento ({removido}): {lista}")
    removido = lista.excluirPrim()
    print(f"Excluindo primeiro elemento ({removido}): {lista}")
    lista.buscar(20)
    removido = lista.excluirAtual()
    print(f"Excluindo elemento atual ({removido}): {lista}")

    print(f"--- Fim do Teste 1 ---\n")


def teste2():
    print("Teste 2")
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
        print(f"Exceção capturada: {e}")

    print(f"Estado final da Lista2: {lista2} (Tamanho: {lista2.tamanho})")
    print(f"A lista está cheia? {lista2.Cheia()}")
    print(f"--- Fim do Teste 2 ---\n")


if __name__ == "__main__":
    teste1()
    teste2()