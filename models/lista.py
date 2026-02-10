from sqlite3 import Cursor
from typing import Optional, Self, Any
from models.database import Database

class Atividade:
    """
        Classe Para representar tarefa, com metodos para salvar, obter, excluir e  atualizar tarefas com um banco de dados usando a classe Database.
    """
    def __init__(self: Self, titulo_atividade: Optional[str], tipo_de_atividade: Optional[str] = None, id_atividade:Optional[int] = None,)-> None:
        self.titulo_tarefa: Optional[str] = titulo_atividade
        self.tipo_de_atividade: Optional[str]  = tipo_de_atividade
        self.id_atividade: Optional[int] = id_atividade

    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao FROM tarefas WHERE id = ?;'
            params: tuple = (id,)
            resultado = db.buscar_tudo(query, params)
            print(resultado)

            #desenpacotamento de coleção
            [[titulo, tipo]] = resultado

        return cls(id_atividade=id, titulo_atividade=titulo)
        
    def salvar_tarefa(self: Self)-> None:
        with Database() as db:
            query: str = " INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);"
            params: tuple = (self.titulo_tarefa, self.tipo_de_atividade)
            db.executar(query, params)

    @classmethod
    def obter_tarefas(cls) -> list[Self]:
        with Database() as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao, id FROM tarefas;'
            resultados: list[Any] = db.buscar_tudo(query)
            atividades: list[Any] = [cls(titulo, tipo, id) for titulo, tipo, id in resultados]
            return atividades
    
    def excluir_tarefa(self) -> Cursor:
        with Database() as db:
            query: str = 'DELETE FROM tarefas WHERE id = ?;'
            params: tuple = (self.id_atividade,)
            resultado: Cursor = db.executar(query, params)
            return resultado
    
    def atualizar_tarefas(self) -> Cursor:
           with Database() as db:
            query: str = 'UPDATE tarefas SET titulo_tarefa = ?, data_conclusao = ? WHERE id = ?;'
            params: tuple = (self.titulo_tarefa, self.tipo_de_atividade, self.id_atividade)
            resultado: Cursor = db.executar(query, params)
            return resultado
    