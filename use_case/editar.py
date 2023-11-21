from use_case.buscar_por_cod import buscarPorCodigo

def editarProduto(codigo, nome, categoria, preco):
    produto = buscarPorCodigo(codigo)
    if produto:
        produto['codigo'] = codigo
        produto['nome'] = nome
        produto['categoria'] = categoria
        produto['preco'] = preco
    else:
        print('Produto não encontrado! ')