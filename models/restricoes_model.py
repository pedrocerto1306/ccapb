import string
import pandas as pd
from models.model_base import Model_Base


class Restricoes_Model(Model_Base):
    def __init__(self, id: int, nome: string, descricao: string):
        super().__init__(id)
        self.nome = nome
        self.descricao = descricao