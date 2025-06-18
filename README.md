# 👥 GitHub Users API – Extraction & REST API avec FastAPI

## 🎯 Objectif du projet

Ce projet a pour but de créer un pipeline complet de **collecte**, **nettoyage**, puis **exposition** de données GitHub à travers une **API REST sécurisée**.  
Il simule un scénario réel où une entreprise souhaite rendre disponibles des données internes via une API pour ses développeurs ou services partenaires.

### 🔧 Deux grandes étapes :

---

### 1️⃣ Extraction et traitement des utilisateurs GitHub

L'application interroge l'API publique de GitHub pour récupérer les utilisateurs ayant créé leur compte après 2015.  
Pour chaque utilisateur, les données suivantes sont extraites :

- `login`
- `id`
- `avatar_url`
- `created_at`
- `bio`

Les données sont ensuite **nettoyées** et **filtrées** :

- Suppression des doublons (via `id`)
- Exclusion des utilisateurs sans `bio`, sans `avatar_url`, ou dont le compte est trop ancien

✅ Les données filtrées sont stockées dans `data/filtered_users.json`.

---

### 2️⃣ Exposition via une API REST sécurisée

Une API est développée avec **FastAPI** pour permettre :

- ✅ Lister tous les utilisateurs
- 🔍 Rechercher un utilisateur par mot-clé (dans le login ou la bio)
- 👤 Obtenir les détails d’un utilisateur spécifique

L’API utilise une **authentification par token**, simulant une API privée ou interne.

---

## 🗂️ Structure du projet

````

tp-api-c1-c5/
│
├── extract_users.py            # Étape 1 : extraction brute depuis GitHub
├── filtered_users.py           # Étape 2 : nettoyage et filtrage
├── users.json                  # Données brutes
├── data/
│   └── filtered_users.json     # Données filtrées prêtes pour l’API
│
├── api/
│   ├── main.py                 # Lancement de l’API FastAPI
│   ├── models.py               # Schémas Pydantic
│   ├── routes.py               # Endpoints de l’API
│   ├── security.py             # Authentification par token (ou alternative)
│
├── tests/
│   └── test_api.py             # Tests API (bonus)
│
├── requirements.txt            # Bibliothèques à installer
├── .env                        # Token GitHub & Token API
└── README.md                   # Documentation du projet
````

## ✨ Résultat attendu

- ✅ Un fichier `filtered_users.json` propre après extraction et nettoyage
- 🌐 Une API REST locale disponible avec plusieurs endpoints fonctionnels
- 🔒 Une authentification basique par token simulant une API interne sécurisée

---

## 🧠 Compétences mobilisées

- 🔄 Consommation d’API externe (GitHub)
- 📄 Gestion de la pagination et des quotas de requêtes
- 🧹 Traitement, filtrage et validation de données
- 🧱 Architecture Python modulaire et maintenable
- ⚙️ Développement d’API REST avec **FastAPI**
- 🛡️ Sécurisation d’une API via authentification par **token**
