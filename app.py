import os
from modelos.restaurante import Restaurante
from modelos.avaliacao import Avaliacao

class ProgramaExpresso:
    def __init__(self):
        self.restaurantes = [
            Restaurante('Varanda Flower', 'Doceria', True),
            Restaurante('Sabor do Interior', 'Caseira', False),
            Restaurante('Peixe Frito', 'Peixaria', False)
        ]

    def finalizar_app(self):
        os.system("clear")
      
        print("Finalizando o app\n")

    def voltar_menu_principal(self):
        input("Digite uma tecla para voltar ao menu principal: ")

    def mostrar_subtitulo(self, texto):
        os.system("clear")
        linha = '*'*(len(texto))
        print(texto)
    
        print()

    def escolher_opcoes(self):
        self.mostrar_subtitulo  ('''
    𝓻𝓮𝓼𝓽𝓪𝓾𝓻𝓪𝓷𝓽𝓮 𝓮𝔁𝓹𝓻𝓮𝓼𝓼𝓸''')
                               


        print("1 - Cadastrar Restaurante")
        print("2 - Listar Restaurantes")
        print("3 - Ativar/Desativar Restaurante")
        print("4 - Avaliar Restaurante")
        print("5 - Ver Média de Avaliações")
        print("6 - Sair\n")

    def opcao_invalida(self):
        self.mostrar_subtitulo("Opção inválida\n".ljust(20))
        self.voltar_menu_principal()

    def listarRestaurantes(self):
        self.mostrar_subtitulo('Listando os Restaurantes'.ljust(20))
        print("Nome:".ljust(27), "Categoria:".ljust(34), "Status:".ljust(24))
        for restaurante in self.restaurantes:
            print(restaurante)

    def alternar_estado_restaurante(self):
        self.mostrar_subtitulo("Alterando o estado do restaurante".ljust(20))
        self.listarRestaurantes()
        nome_restaurante = input("Digite o nome do Restaurante que desejas alterar: ")
        restaurante_encontrado = False

        for restaurante in self.restaurantes:
            if nome_restaurante == restaurante.nome:
                restaurante_encontrado = True
                mensagem = restaurante.ativar_desativar()
                print(mensagem)
                break

        if not restaurante_encontrado:
            print("O restaurante não foi encontrado.")

        self.voltar_menu_principal()

    def avaliacao(self):
        self.mostrar_subtitulo("Avaliar Restaurante\n".ljust(20))
        self.listarRestaurantes()

        nome_restaurante = input("Digite o nome do restaurante que deseja avaliar: ")
        restaurante_encontrado = False

        for restaurante in self.restaurantes:
            if nome_restaurante == restaurante.nome:
                restaurante_encontrado = True
                while True:
                    nota = int(input("Digite uma nota de 1 a 5 para avaliar este restaurante: "))
                    if 1 <= nota <= 5:
                        restaurante.adicionar_avaliacao(nota)
                        print(f"Você avaliou o restaurante {nome_restaurante} com a nota {nota}.")
                        break
                    else:
                        print("Por favor, digite uma nota válida (entre 1 e 5).")

        if not restaurante_encontrado:
            print("Restaurante não encontrado.")

        self.voltar_menu_principal()

    def ver_media_avaliacoes(self):
        self.mostrar_subtitulo("Média de Avaliações dos Restaurantes\n".ljust(20))
        for restaurante in self.restaurantes:
            print(restaurante.calcular_media_avaliacoes())

        self.voltar_menu_principal()

    def cadastrar_novo_restaurante(self):
        nome_do_restaurante = input("Digite o nome do novo restaurante: ")
        categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
        restaurante_novo = Restaurante(nome_do_restaurante, categoria)
        self.restaurantes.append(restaurante_novo)
        print(f"Você cadastrou o restaurante: {nome_do_restaurante}")

    def main(self):
        while True:
            try:
                self.escolher_opcoes()
                opcao_digitada = int(input("Digite a opção desejada: "))
                if opcao_digitada == 1:
                    print("Você escolheu cadastrar restaurante\n" )
                    self.cadastrar_novo_restaurante()
                elif opcao_digitada == 2:
                    self.listarRestaurantes()
                    self.voltar_menu_principal()
                elif opcao_digitada == 3:
                    self.alternar_estado_restaurante()
                elif opcao_digitada == 4:
                    self.avaliacao()
                elif opcao_digitada == 5:
                    self.ver_media_avaliacoes()
                elif opcao_digitada == 6:
                    print("Você escolheu sair do aplicativo\n")
                    self.finalizar_app()
                    break
                else:
                    self.opcao_invalida()
            except ValueError:
                print("Por favor, digite um número válido.")

if __name__ == "__main__":
    programa = ProgramaExpresso()
    programa.main()
