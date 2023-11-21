from use_case.gerar_produto import criarProduto
from repositorio import banco
# codigo - nome - categoria - preço
def adicionarProduto(nome, categoria, preço):
    produto = criarProduto(nome, categoria, preço)
    banco.append(produto)
    print('Produto adicionado com sucesso!')
