from sqlite3 import Cursor
from typing import Optional, Self, Any
from models.database import Database

class Atividade:
    """
        Classe Para representar tarefa, com metodos para salvar, obter, excluir e  atualizar tarefas com um banco de dados usando a classe Database.
    """
    def __init__(self: Self, titulo_atividade: Optional[str], tipo_de_atividade: Optional[str] = None, id_atividade:Optional[int] = None,)-> None:
        self.titulo_atividade: Optional[str] = titulo_atividade
        self.tipo_de_atividade: Optional[str]  = tipo_de_atividade
        self.id_atividade: Optional[int] = id_atividade

    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
            query: str = 'SELECT titulo_atividade, tipo_de_atividade FROM atividades WHERE id = ?;'
            params: tuple = (id,)
            resultado = db.buscar_tudo(query, params)
            print(resultado)

            #desenpacotamento de coleção
            [[titulo, tipo]] = resultado

        return cls(id_atividade=id, titulo_atividade=titulo, tipo_de_atividade=tipo)
        
    def salvar_atividade(self: Self)-> None:
        with Database() as db:
            query: str = " INSERT INTO atividades (titulo_atividade, tipo_de_atividade) VALUES (?, ?);"
            params: tuple = (self.titulo_atividade, self.tipo_de_atividade)
            db.executar(query, params)

    @classmethod
    def obter_atividades(cls) -> list[Self]:
        with Database() as db:
            query: str = 'SELECT titulo_atividade, tipo_de_atividade, id FROM atividades;'
            resultados: list[Any] = db.buscar_tudo(query)
            atividades: list[Any] = [cls(titulo, tipo, id) for titulo, tipo, id in resultados]
            return atividades
    
    def excluir_atividade(self) -> Cursor:
        with Database() as db:
            query: str = 'DELETE FROM atividades WHERE id = ?;'
            params: tuple = (self.id_atividade,)
            resultado: Cursor = db.executar(query, params)
            return resultado
    
    def atualizar_atividade(self) -> Cursor:
           with Database() as db:
            query: str = 'UPDATE atividades SET titulo_atividade = ?, tipo_de_atividade = ? WHERE id = ?;'
            params: tuple = (self.titulo_atividade, self.tipo_de_atividade, self.id_atividade)
            resultado: Cursor = db.executar(query, params)
            return resultado
    