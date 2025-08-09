# Labo 01 – Client/Serveur, Persistence (DAO/RDBS/NoSQL)
<img src="https://upload.wikimedia.org/wikipedia/commons/2/2a/Ets_quebec_logo.png" width="250">    
ÉTS - LOG430 - Architecture logicielle - Chargé de laboratoire: Gabriel C. Ullmann, Automne 2025.    

## 🎯 Objectifs d’apprentissage

- Apprendre à créer une application client-serveur simple.
- Comprendre et mettre en œuvre la structure **MVC avec DAO** pour bien séparer les responsabilités.
- Comprendre les avantages et les inconvénients des bases de données relationnelles (ex. MySQL) par rapport aux bases orientées documents (ex. MongoDB).

---

## ⚙️ Setup

### 1. Faites un fork et clonez le dépôt GitLab

```bash
git clone https://github.com/guteacher/log430-a25-labo1
cd log430-a25-labo1
```

### 2. Lancez le conteneur Docker

```bash
docker compose up -d
```

Vérifie que le conteneur est bien lancé :

```bash
docker ps
```

### 3. Créez un environnement virtuel Python sur votre ordinateur (pas dans Docker)

#### Sur Linux/Mac
```bash
python -m venv .venv/labo0
source .venv/labo0/bin/activate
```

#### Sur Windows
```bash
python -m venv .venv/labo0
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser # Si nécessaire
.venv\labo0\Scripts\activate.ps1
```

### 4. Installez les dépendances Python

```bash
pip install -r requirements.txt
```

### 5. Lancez l’application

```bash
python app.py
```

---

## 🧪 Activités pratiques

### 1. DAO MySQL

Le fichier `UserDAO` (dans `dao/user_dao.py`) contient déjà les méthodes `select_all()` et `insert(user)`.

Complétez cette DAO en y ajoutant :
   - `update(user)` – pour modifier un utilisateur existant.
   - `delete(user_id)` – pour supprimer un utilisateur.

### 2. DAO MongoDB

Créez une nouvelle DAO `UserDAOMongo` dans un fichier `dao/user_dao_mongo.py`.

Implémentez les mêmes méthodes :
   - `select_all()`
   - `insert(user)`
   - `update(user)`
   - `delete(user_id)`

Modifiez `test_user.py` pour utiliser `UserDAOMongo` en lieu de `UserDAO`, puis relancez les tests. Une implémentation correcte doit produire les mêmes résultats, en considérant que quelques ajustements mineurs dans les tests peuvent être nécessaires pour assurer l’interchangeabilité des DAO.

> 💡 Réfléchissez : quels sont les avantages de placer le code d’accès à la base de données dans une DAO plutôt que, par exemple, dans un modèle, un contrôleur ou d’autres classes ?

### 3. Nouveau tableau : Products
Insérez le code SQL pour créer le tableau `products` dans `db-init/init.sql`. Ce fichier sera executé a chaque fois qu'on démarre la conteneur.
```sql
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    brand VARCHAR(20) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);
```

Créez un nouvel Model, View, Controller et DAO pour `Product`. Utilisez une structure similaire à `User`. Ajoutez les options `Montrer la liste d'items` et `Ajouter un item` dans `app.py`.

> 💡 Réfléchissez : si nous devions créer un système de magasin capable de faire la gestion d'achats des utilisateurs (Products et Users), comment structurerions-nous nos données dans MySQL par rapport à MongoDB ?


### ✅ Correction des activités

Des tests unitaires sont inclus dans le dépôt. Pour les exécuter :

```bash
python3 -m pytest
```

Si tous les tests passent ✅, vos implémentations sont correctes.

---

## 📦 Livrables

- Fichier `.zip` contenant :
  - l'ensemble du code source du projet Labo 01
  - 5 diagrammes UML de l'application (use case, classes, sequence, activity, deployment)

- Un **rapport en PDF** , contenant :
  - Une brève explication de votre structure MVC.
  - Une comparaison entre MySQL et MongoDB (avantages/inconvénients dans le contexte du projet).

