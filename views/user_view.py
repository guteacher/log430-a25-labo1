"""
User view
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

class UserView:
    def show_users(users):
        print("Liste d'utilisateurs :")
        for user in users:
            print(f"{user.id}: {user.name} ({user.email})")

    def get_inputs():
        name = input("Nom d'utilisateur : ")
        email = input("Adresse courriel : ")
        return name, email
