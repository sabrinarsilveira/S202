from database import Database
from livroModel import LivroModel

def exibir_menu():
    print("\n=== MENU ===")
    print("1. Adicionar Livro")
    print("2. Listar Livros")
    print("3. Atualizar Livro")
    print("4. Deletar Livro")
    print("5. Sair")


def main():
    db = Database(database="Biblioteca", collection="Livros")
    livroModel = LivroModel(database=db)

    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor: ")
            ano = int(input("Digite o ano de publicação do livro: "))
            preco = float(input("Digite o preço do livro: "))
            livroModel.create_livro(titulo, autor, ano, preco)


        elif opcao == "2":
            livros = livroModel.read_all_livros()
            if livros:
                for livro in livros:
                    print(f"ID: {livro['_id']}, Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Preço: {livro['preco']}")
            else:
                print("Não há livros na colecao.")


        elif opcao == "3":
            livro_id = input("Digite o ID do livro que deseja atualizar: ")
            titulo = input("Digite o novo título do livro: ")
            autor = input("Digite o novo nome do autor: ")
            ano = int(input("Digite o novo ano de publicacao do livro: "))
            preco = float(input("Digite o novo preco do livro: "))
            livroModel.update_livro(livro_id, titulo, autor, ano, preco)

        elif opcao == "4":
            livro_id = input("Digite o ID do livro que deseja deletar: ")
            livroModel.delete_livro(livro_id)

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opcao inválida. Tente novamente.")

if __name__ == "__main__":
    main()