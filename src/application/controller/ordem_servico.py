from application.model.ordem_servico import OrdemServicoModel

class OrdemServicoController:
    def __init__(self):
        self.repository = OrdemServicoRepository()

    def criar_os(self):
        os = OrdemServicoModel(nome, telefone, placa, modelo, descricao, valor_mao_obra, valor_pecas)

        return self.repository.inserir(os)
