from database.connection import get_connection

def create_table():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS ordem_servico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT not null,
                telefone TEXT not null,
                placa TEXT not null,
                modelo TEXT not null,
                descricao TEXT not null,
                valor_mao_obra REAL not null,
                valor_pecas REAL not null,
                data TEXT default CURRENT_TIMESTAMP,
                status TEXT not null DEFAULT 'aberta' CHECK (status IN ('aberta', 'em_andamento', 'concluida', 'cancelada'))
            )
        """)