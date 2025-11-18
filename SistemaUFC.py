
class Curso:
    def __init__(self, nome_curso, vagas_total):  #método construtor
        self.nome_curso = nome_curso
        self.vagas_total = vagas_total
        self.vagas_ocupadas = 0 
               

class Campus:
    def __init__(self, nome, localizacao):
        self.nome = nome
        self.localizacao = localizacao
        self.cursos = []
lista_campus_ufc = []

def novo_campus():
    print("====Criar novo campus====")
    nome = input("Insira o nome do Campus:\n ")
    localizacao = input("Insira a localização:\n ") 
    for campus_existente in lista_campus_ufc:
        if campus_existente.nome.lower() == nome.lower():
            print(f"O Campus '{nome}' já existe. Tente outro nome.")
            return 
    novo_campus = Campus(nome, localizacao)
    lista_campus_ufc.append(novo_campus)
    print(f"Campus {nome} criado com sucesso!\n")

def listar_campus():
    if not lista_campus_ufc:
        print("Nenhum Campus cadastrado no sistema.")
        return None

    print("\nCampi disponíveis:")
    contador = 1
    for campus in lista_campus_ufc:
        print(f"[{contador}] Nome: {campus.nome}, Local: {campus.localizacao}")
        contador = contador + 1 
        
    while True:
        entrada_usuario = input("Escolha o NÚMERO do Campus (ou 0 para cancelar):\n ")
        
        if entrada_usuario == '0':
            print("Seleção cancelada.")
            return None

        if entrada_usuario.isdigit():
            numero_campus = int(entrada_usuario)
            
            if 1 <= numero_campus <= len(lista_campus_ufc):
                indice_campus = numero_campus - 1
                return lista_campus_ufc[indice_campus]
            else:
                print("Opção inválida, o número não está na lista.")
        else:
            print("Por favor, digite apenas um número.")
    
def adicionar_curso():
    print("\n==== Adicionar novo Curso ====")
    campus_selecionado = listar_campus()
    if campus_selecionado is None:
        return 
    nome_curso = input("Insira o nome do Curso:\n ") 
    vagas_total = int(input("Insira o total de vagas:\n "))

    for curso in campus_selecionado.cursos: 
        if curso.curso == nome_curso:
            print(f"O Curso '{nome_curso}' já existe no Campus '{campus_selecionado.nome}'.")
            return
    novo_curso = Curso(nome_curso, vagas_total) 
    campus_selecionado.cursos.append(novo_curso) 
    
    print(f"Curso {nome_curso} criado com sucesso!")


def listar_cursos_campus(): 
    print("\n==== Lista de Cursos por Campus ====")
    campus_selecionado = listar_campus()
    if campus_selecionado is None:
        return 
    print(f"Cursos no Campus '{campus_selecionado.nome}':")
    if not campus_selecionado.cursos:
        print("Nenhum curso cadastrado neste campus.")
    else:
        for curso in campus_selecionado.cursos:
            print(f"Curso: {curso.nome_curso}, Vagas Totais: {curso.vagas_total}, Vagas Ocupadas: {curso.vagas_ocupadas}")


def editar_curso():
    print("\n====Editar Curso====")
    campus_selecionado = listar_campus()
    if len(campus_selecionado.cursos) == 0:
        print(f"O Campus {campus_selecionado.nome} não tem cursos para editar.")
        return
    
    print(f"\n--- Cursos para editar no Campus: {campus_selecionado.nome} ---")
    
    #mostra os cursos disponíveis
    contador_curso = 1
    for curso in campus_selecionado.cursos:
        print(f"[{contador_curso}] {curso.nome_curso} | Vagas: {curso.vagas_total} / Ocupadas: {curso.vagas_ocupadas}")
        contador_curso = contador_curso + 1
        

    while True:
        entrada_curso = input("\nDigite o NÚMERO do Curso que você quer mudar (ou 0 para cancelar):\n ")
        
        if entrada_curso == '0':
            print("Edição de curso cancelada.")
            return

        if entrada_curso.isdigit():
            numero_curso = int(entrada_curso)
            
         
            if 1 <= numero_curso <= len(campus_selecionado.cursos):
                
                indice_curso = numero_curso - 1
                curso_a_editar = campus_selecionado.cursos[indice_curso]
                break 
            else:
                print("Opção inválida, o número não está na lista.")
        else:
            print(" Por favor, digite apenas um número.")

    print(f"\n--- Editando: {curso_a_editar.nome_curso} ---")
    print("Se quiser manter o valor, apenas pressione ENTER.")
    

    novo_nome = input(f"Novo nome (Atual: {curso_a_editar.nome_curso}): ")
    if novo_nome != "": 
        curso_a_editar.nome_curso = novo_nome
        
    while True:
        nova_vagas_str = input(f"Novas vagas totais (Atual: {curso_a_editar.vagas_total}): ")
        
        if nova_vagas_str == "": 
            break
            
        if nova_vagas_str.isdigit():
            nova_vagas = int(nova_vagas_str)

            if nova_vagas >= curso_a_editar.vagas_ocupadas:
                curso_a_editar.vagas_total = nova_vagas
                break
            else:
                print(f"As novas vagas não podem ser menores que as vagas ocupadas ({curso_a_editar.vagas_ocupadas}).")
        else:
            print("Digite apenas números.")

    print("\n---")
    print(f"Curso '{curso_a_editar.nome_curso}' editado com sucesso!")
    print(f"Novo status: Vagas Totais: {curso_a_editar.vagas_total}")
    print("---")


def excluir_curso():
    print("\n====Excluir Curso====")
    campus_selecionado = listar_campus()
    if campus_selecionado is None:
        return
    if len(campus_selecionado.cursos) == 0:
        print(f"O Campus {campus_selecionado.nome} não tem cursos para excluir.")
        return
    print(f"\n--- Cursos disponíveis no Campus: {campus_selecionado.nome} ---")
    contador_curso = 1
    for curso in campus_selecionado.cursos:
        print(f"[{contador_curso}] {curso.nome_curso} | Vagas: {curso.vagas_total}")
        contador_curso = contador_curso + 1
    while True:
        entrada_curso = input("\nDigite o NÚMERO do Curso que você quer EXCLUIR (ou 0 para cancelar):\n ")
        if entrada_curso == '0':
            print("Exclusão de curso cancelada.")
            return
        if entrada_curso.isdigit():
            numero_curso = int(entrada_curso)
            if 1 <= numero_curso <= len(campus_selecionado.cursos):
                indice_curso = numero_curso - 1
                curso_excluido = campus_selecionado.cursos[indice_curso]
                nome_curso = curso_excluido.nome_curso
                campus_selecionado.cursos.pop(indice_curso) 

                print("\n---")
                print(f"Curso '{nome_curso}' EXCLUÍDO com sucesso do Campus {campus_selecionado.nome}.")
                print("---")
                return
                
            else:
                print(" Opção inválida, o número não está na lista.")
        else:
            print(" Por favor, digite apenas um número.")

def excluir_campus():
    print("\n====Excluir Campus====")
    if len(lista_campus_ufc) == 0:
        print("Ainda não há Campi cadastrados para excluir.")
        return
    print("\n--- Campi disponíveis para exclusão ---")
    contador_campus = 1
    for campus in lista_campus_ufc:
        print(f"[{contador_campus}] Nome: {campus.nome}, Local: {campus.localizacao}")
        contador_campus = contador_campus + 1
    while True:
        entrada_campus = input("\nDigite o NÚMERO do Campus que você quer EXCLUIR (ou 0 para cancelar):\n ")
        if entrada_campus == '0':
            print("Exclusão de Campus cancelada.")
            return

        if entrada_campus.isdigit():
            numero_campus = int(entrada_campus)
    
            if 1 <= numero_campus <= len(lista_campus_ufc):
                
                indice_campus = numero_campus - 1
                campus_excluido = lista_campus_ufc[indice_campus]
                lista_campus_ufc.pop(indice_campus) 
                
                print("\n---")
                print(f" Campus '{campus_excluido.nome}' e todos os seus cursos EXCLUÍDOS com sucesso.")
                print("---")
                return 
                
            else:
                print(" Opção inválida, o número não está na lista.")
        else:
            print("Por favor, digite apenas um número.")


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