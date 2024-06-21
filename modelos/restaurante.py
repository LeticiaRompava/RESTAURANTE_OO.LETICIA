class Restaurante:
    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.avaliacoes = []

    def ativar_desativar(self):
        self.ativo = not self.ativo
        if self.ativo:
            return f'O restaurante {self.nome} foi ativado com sucesso.'
        else:
            return f'O restaurante {self.nome} foi desativado com sucesso.'

    def adicionar_avaliacao(self, nota):
        self.avaliacoes.append(nota)

    def calcular_media_avaliacoes(self):
        if not self.avaliacoes:
            return "Sem avaliações ainda."
        else:
            media = sum(self.avaliacoes) / len(self.avaliacoes)
            return f'{self.nome}    Média de estrelas: {media:.2f} ({len(self.avaliacoes)} avaliações)'

    def __str__(self):
        return f'Nome: {self.nome.ljust(20)}  Categoria: {self.categoria.ljust(22)}  Status: {"Ativado" if self.ativo else "Desativado"}'

