
from campus import novo_campus
from campus import listar_campus
from campus import excluir_campus
from cursos import adicionar_curso
from cursos import listar_cursos_campus
from cursos import editar_curso
from cursos import excluir_curso


def menu():
    while True:
        print("=== Sistema UFC ===")
        print("1. Novo Campus") #
        print("2. Adicionar Curso") #
        print("3. Listar Cursos") #
        print("4. Editar Curso") #
        print("5. Excluir Curso") #
        print("6. Excluir Campus") #
        print("7. Listar Campus") #
        print("8. Sair")

        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            novo_campus()
        elif opcao == "2":
            adicionar_curso()
        elif opcao == "3":
            listar_cursos_campus()
        elif opcao == "4":
            editar_curso()
        elif opcao == "5":
            excluir_curso()
        elif opcao == "6":
            excluir_campus()
        elif opcao == "7":
            listar_campus()
        elif opcao == "8":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
