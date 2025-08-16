"""
Application example - MVC avec 2 bases de données
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from controllers.user_controller import UserController

class Application:
    def run(self):
        print("Application de Gestion de Magasin - Labo 01")
        print("=======================")
        controller = UserController()

        while True:
            print("\n1. Montrer la liste d'utilisateurs\n2. Ajouter un utilisateur\n3. Quitter l'appli")
            choice = input("Choisissez une option: ")

            if choice == '1':
                controller.list_users()
            elif choice == '2':
                controller.create_user()
            elif choice == '3':
                controller.shutdown()
                break
            else:
                print("Cette option n'existe pas.")

if __name__ == '__main__':
    app = Application()
    app.run()
