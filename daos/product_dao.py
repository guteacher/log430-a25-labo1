"""
Product DAO (Data Access Object)
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

import mysql.connector
from models.user import User

class ProductDAO:
    def __init__(self):
        # NOTE: Normalement, les informations d'identification ne devraient pas être dans le code. Il s'agit d'une simplification.
        self.conn = mysql.connector.connect(
            host='localhost',
            user='user',
            password='pass',
            database='mydb'
        )
        self.cursor = self.conn.cursor()

    def select_all(self):
        pass

    def insert(self, user):
        pass

    def update(self, user):
        pass

    def delete(self, user_id):
        pass

    def delete_all(self): #optionnel
        pass
        
    def close(self):
        self.cursor.close()
        self.conn.close()
