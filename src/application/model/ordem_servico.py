class OrdemServicoModel:
    def __init__(self, nome, telefone, placa, modelo, descricao,
                 valor_mao_obra=0, valor_pecas=0, status="aberta"):
        self.nome = nome
        self.telefone = telefone
        self.placa = placa
        self.modelo = modelo
        self.descricao = descricao
        self.valor_mao_obra = valor_mao_obra
        self.valor_pecas = valor_pecas
        self.status = status