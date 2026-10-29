import sqlite3
from database.init_db import create_table
from application.controller.ordem_servico import OrdemServicoController

controller = OrdemServicoController()

def main():
    loop = True

    while loop:
        try:
            create_table()
        except sqlite3.OperationalError as e:
            print(f"❌ Erro de conexão ou operação no SQLite: {e}")

        print("""Olá Usuário! Escolha uma opção:

    1- Cadastro de Ordem de Serviço.
    2- Listar Veículos.
    3- Atualizar Ordem de Serviço.
    4- Excluir Ordem de Serviço.
        
[Clique ENTER para sair.]""")

        opt = input("-> ")

        match opt:
            case "1":
                nome = input("Nome do cliente: ")
                telefone = input("Telefone: ")
                placa = input("Placa: ").upper()
                modelo = input("Modelo: ")
                descricao = input("Descrição do serviço: ")
                valor_mao_obra = float(input("Valor da mão de obra: "))
                valor_pecas = float(input("Valor das peças: "))
                
                try:
                    id_os = controller.criar_os(nome, telefone, placa, modelo,
                                            descricao, valor_mao_obra, valor_pecas)
                    print(f"✅ Ordem de serviço #{id_os} criada!")
                except sqlite3.OperationalError as e:
                    print(f"❌ Erro no SQLite: {e}")

            case "":
                print("Obrigado por usar!")
                loop = False


if __name__ == "__main__":
    main()