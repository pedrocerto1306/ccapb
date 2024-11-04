import string
import pandas as pd
from models.model_base import Model_Base


class Login_Model(Model_Base):
    def __init__(self, id: int, username: string, password: string):
        super().__init__(id)
        self.username = username
        self.password = password