<div align="center">

# Cédric KOUADIO

**Data Analyst · Data Scientist · Data Engineer**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-cedric--kouadio--dev-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/cedric-kouadio-dev)
[![Email](https://img.shields.io/badge/Email-cedric.kouadio.dev%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:cedric.kouadio.dev@gmail.com)
[![CV en ligne](https://img.shields.io/badge/CV-gomugomuno01.github.io%2Fcv-1a1a2e?style=flat-square&logo=github&logoColor=white)](https://gomugomuno01.github.io/cv/)

</div>

---

Étudiant en **Mastère Informatique, IA & Big Data** à l'ESGI Paris. J'ai passé deux ans à construire les applications qui produisent la donnée ; aujourd'hui, je l'analyse. Connaître les deux côtés change ma façon de travailler : je comprends à la fois comment une donnée est produite et comment la transformer en décision.

Je cherche une **alternance à partir de septembre 2026** en Île-de-France, sur des sujets Data Analyst, Data Scientist ou Data Engineer. La plupart des projets ci-dessous sont en ligne et testables en un clic.

---

## À tester tout de suite

| | Projet | Ce que ça fait |
|---|---|---|
| ▶ | [**Démo · Chatbot RAG**](https://gomugomuno01-chatbot-rag.hf.space/) | Posez une question sur n'importe quel document, réponse en moins de 2 s |
| ▶ | [**Colab · Sales Report**](https://colab.research.google.com/github/GomuGomuNo01/sales-report-automation/blob/main/demo_colab.ipynb) | Un CSV en entrée, un rapport PDF complet en 7 s |
| ▶ | [**Codespaces · Automatisations**](https://github.com/codespaces/new/GomuGomuNo01/automatisation-de-processus) | 6 automatisations métier, environnement prêt à l'emploi |
| ▶ | [**Swagger · API REST JWT**](https://jwt-api-gkdg.onrender.com/swagger-ui.html) | API sécurisée déployée, documentation interactive |

---

## Projets Data & IA

### [NYC Taxi Data Engineering Pipeline](https://github.com/GomuGomuNo01/nyc-taxi-data-engineering) *(en cours)*

Pipeline PySpark qui transforme 500 000 lignes de courses new-yorkaises brutes en données fiables et exploitables, selon une architecture en couches (Bronze/Silver/Gold). Chaque rejet est audité et documenté plutôt qu'ignoré : 2,3 % de lignes invalides tracées.

`Python` `PySpark` `Star Schema` `ETL`

### [Maven Toys Analytics](https://github.com/GomuGomuNo01/maven-toys-powerbi-analytics)

Dashboard Power BI pour une enseigne de 50 magasins. Révèle que la marge ne suit pas la hausse du chiffre d'affaires, avec 29 069 $ perdus chaque mois à cause des ruptures de stock. 829 262 ventes analysées, 66 mesures DAX, modélisation en étoile.

`Power BI` `DAX` `Power Query`

### [Contoso Sales Analytics](https://github.com/GomuGomuNo01/contoso-sales-powerbi)

Dashboard Power BI qui révèle une baisse de chiffre d'affaires de 33 % (43,8M$ → 29,3M$) et identifie les catégories de produits les plus touchées. 225 000 ventes analysées, 30 mesures DAX.

`Power BI` `DAX` `Power Query`

### [SBS Bank](https://github.com/GomuGomuNo01/Simple-Banking-System-Python)

Analyse de 18 mois d'activité d'une néobanque simulée (1 800 clients, 254 000 opérations). Révèle que les clients apportés par des partenaires activent leur compte 2,4 fois moins souvent que les autres (test du khi-deux, p<0,001), avec 6 recommandations documentées.

`Python` `SQL` `Segmentation RFM` `Tests statistiques`

### [Telco Churn Prediction](https://github.com/GomuGomuNo01/telco-churn-prediction)

Compare 9 modèles de machine learning sur 7 043 clients télécoms pour anticiper la résiliation. Modèle retenu (Naive Bayes, recall 73,3 %) après arbitrage coût métier plutôt qu'optimisation brute de l'accuracy, déployé dans une application Streamlit.

`Python` `scikit-learn` `Streamlit`

### [Chatbot RAG · DocAssist](https://github.com/GomuGomuNo01/Chatbot-RAG)

Recherche documentaire en langage naturel. Les documents sont découpés et indexés dans une base vectorielle, les passages pertinents sont récupérés à la volée, puis une réponse sourcée est générée, avec refus de répondre si l'information n'y figure pas. Précision supérieure à 85 %, réponse en moins de 2 secondes.

`Python` `LangChain` `FAISS` `FastAPI`

### [Career-Ops](https://github.com/GomuGomuNo01/career-ops)

Système de recherche d'emploi bâti sur Claude Code. Il analyse une annonce, en extrait les exigences, génère les documents de candidature correspondants et met à jour un tableau de suivi. 14 modes spécialisés, serveurs MCP connectés à des outils maison.

`Claude Code` `MCP` `Python` `Go`

---

## Projets Développement (le socle qui explique ma lecture de la donnée)

### [Sales Report Automation](https://github.com/GomuGomuNo01/sales-report-automation)

Chaîne de traitement qui remplace la mise en forme manuelle de rapports commerciaux. Lit des exports CSV hétérogènes, applique des contrôles de cohérence, calcule les agrégations et produit un PDF de 6 pages en 7 secondes (contre 5 heures à la main). Plus de 50 tests automatisés.

`Python` `pandas` `reportlab` `pytest`

### [Automatisation de Processus](https://github.com/GomuGomuNo01/automatisation-de-processus)

Six automatisations métier en service en entreprise depuis deux ans : suivi de stock, envois d'e-mails SMTP et collecte de données web. Chaque traitement est planifié, journalisé et reproductible.

`Python` `Selenium` `Playwright` `openpyxl`

### [API REST JWT · Spring Boot](https://github.com/GomuGomuNo01/api-rest-jwt)

API REST sécurisée illustrant une architecture en couches Controller / Service / Repository. Authentification par JWT, gestion des droits par rôle, documentation Swagger interactive et tests JUnit.

`Java` `Spring Boot` `Spring Security` `JUnit`

### [Mini-CRM](https://github.com/GomuGomuNo01/mini_crm)

Application web de gestion de la relation client : suivi des clients et des contrats, architecture MVC et accès aux données via un ORM. Construite sur ASP.NET Core 8 avec Entity Framework Core et MySQL.

`C#` `ASP.NET Core 8` `EF Core` `MySQL`

### [Hospital](https://github.com/GomuGomuNo01/Hospital)

Système de gestion hospitalière centré sur la confidentialité des données de santé : dossiers patients, trois rôles aux droits strictement distincts, authentification à deux facteurs et journal d'audit inaltérable.

`Laravel` `PHP` `Blade` `MySQL`

---

## Stack technique

**Data & Analyse**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)

SQL avancé (CTE, fonctions de fenêtrage, vues analytiques) · DAX et modélisation en étoile · statistiques appliquées (test du khi-deux, segmentation RFM) · nettoyage, structuration et contrôle qualité de données

**IA Générative & Agents**

![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-0467DF?style=flat-square&logo=meta&logoColor=white)
![Claude](https://img.shields.io/badge/Claude-D97757?style=flat-square&logo=anthropic&logoColor=white)
![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-Model_Context_Protocol-1a1a2e?style=flat-square)

RAG, prompt engineering, serveurs MCP connectés à des outils maison, utilisation quotidienne de Claude Code

**Développement (le socle qui explique ma lecture de la donnée)**

![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![C#](https://img.shields.io/badge/C%23-512BD4?style=flat-square&logo=dotnet&logoColor=white)
![Laravel](https://img.shields.io/badge/Laravel-FF2D20?style=flat-square&logo=laravel&logoColor=white)
![PHP](https://img.shields.io/badge/PHP-777BB4?style=flat-square&logo=php&logoColor=white)

**Bases de données**

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL_Server-CC2927?style=flat-square&logo=microsoftsqlserver&logoColor=white)

**Outils & DevOps**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

---

## Formation

| Diplôme | Établissement | Période |
|---------|---------------|---------|
| Mastère Informatique, IA & Big Data *(alternance)* | ESGI Paris | sept. 2026 → |
| Mastère Informatique, IA & Management de projet numérique | ESIIA Torcy | 2025–2026 |
| Licence Professionnelle Réseaux & Génie Logiciel | PIGIER Côte d'Ivoire | 2021–2024 |
| BTS Développement d'Applications | PIGIER Côte d'Ivoire | 2021–2022 |

---

<div align="center">

📍 **Île-de-France (Paris & région)** · Alternance dès **septembre 2026** · rythme 3 semaines entreprise / 1 semaine école

[![LinkedIn](https://img.shields.io/badge/Contactez--moi_sur_LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/cedric-kouadio-dev)

</div>
