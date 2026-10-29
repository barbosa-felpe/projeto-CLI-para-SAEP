from database.connection import get_connection

class OrdemServicoRepository:
    def inserir(self, os):
        with get_connection as conn:
            cursor = conn.execute(
                """INSERT INTO ordem_servico 
                (nome, telefone, placa, modelo, descricao, valor_mao_obra, valor_pecas, status)
                VALUES (?,?,?,?,?,?,?,?)""", (os.nome, os.telefone, os.placa, os.modelo, 
                os.descricao, os.valor_mao_obra, os.valor_pecas, os.status),
            )
            return cursor.lastrowidL