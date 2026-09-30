<div align="center">

# Cédric KOUADIO

**Data Analyst · Data Scientist · Data Engineer**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-cedric--kouadio--dev-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/cedric-kouadio-dev)
[![Email](https://img.shields.io/badge/Email-cedric.kouadio.dev%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:cedric.kouadio.dev@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-cedric--kouadio--portfolio.onrender.com-1a1a2e?style=flat-square&logo=render&logoColor=white)](https://cedric-kouadio-portfolio.onrender.com)

</div>

---

## À propos

Étudiant en **Mastère Intelligence Artificielle & Big Data** à l'ESGI Paris, après une Licence Professionnelle Réseaux & Génie Logiciel et un BTS Développement d'Applications en Côte d'Ivoire.

Le code m'a d'abord attiré par ce qu'il permet de construire. J'ai commencé par développer des applications, puis je me suis spécialisé dans l'analyse de données : ce passage m'a appris à voir une donnée de bout en bout, depuis sa production dans le code jusqu'à la décision qu'elle permet de prendre. C'est cette continuité, entre le terrain technique et l'analyse, que j'essaie de mettre dans chaque projet ci-dessous.

Ce qui m'intéresse aujourd'hui : transformer des données brutes en réponses claires à une question métier, avec des outils qui tournent vraiment, pas des prototypes qui dorment. La plupart des projets ci-dessous sont en ligne et testables en un clic.

---

## À tester tout de suite

| | Projet | Ce que ça fait |
|---|---|---|
| ▶ | [**Démo · Chatbot RAG**](https://gomugomuno01-chatbot-rag.hf.space/) | Posez une question sur n'importe quel document, réponse sourcée en moins de 2 s |
| ▶ | [**Dashboard · NYC Taxi**](https://github.com/GomuGomuNo01/nyc-taxi-analyse-revenus/releases/latest/download/NYC_Taxi_Dashboard.pbix) | Fichier Power BI prêt à l'emploi, données incluses |
| ▶ | [**Colab · Sales Report**](https://colab.research.google.com/github/GomuGomuNo01/sales-report-automation/blob/main/demo_colab.ipynb) | Un CSV en entrée, un rapport PDF complet en 7 s |
| ▶ | [**Codespaces · Automatisations**](https://github.com/codespaces/new/GomuGomuNo01/automatisation-de-processus) | 6 automatisations métier, environnement prêt à l'emploi |
| ▶ | [**Swagger · API REST JWT**](https://jwt-api-gkdg.onrender.com/swagger-ui.html) | API sécurisée déployée, documentation interactive |

---

## Projets Data & IA

### [NYC Taxi — où positionner les chauffeurs ?](https://github.com/GomuGomuNo01/nyc-taxi-analyse-revenus)

Une compagnie de taxis veut savoir où et quand positionner ses chauffeurs pour maximiser leur revenu par heure. L'analyse de 7,7 millions de courses réelles (New York, 2019) répond à cette question et débouche sur un dashboard Power BI, validé par 26 tests automatisés.

`Python` `PySpark` `SQL` `Power BI` `DAX`

### [Maven Toys Analytics](https://github.com/GomuGomuNo01/maven-toys-powerbi-analytics)

Une enseigne de 50 magasins voit son chiffre d'affaires progresser, mais pas sa marge. L'analyse de 829 262 ventes révèle que les ruptures de stock lui coûtent 29 069 $ par mois, et le dashboard Power BI (66 mesures DAX) transforme ce constat en recommandations chiffrées.

`Power BI` `DAX` `Power Query` `Python`

### [Contoso Sales Analytics](https://github.com/GomuGomuNo01/contoso-sales-powerbi)

Le chiffre d'affaires d'un distributeur recule de 33 % (43,8M$ → 29,3M$), sans explication claire. L'analyse de 225 000 ventes identifie les catégories de produits les plus touchées, et le dashboard Power BI associé (30 mesures DAX) rend ce diagnostic lisible pour la direction commerciale.

`Power BI` `DAX` `Power Query` `Python`

### [SBS Bank](https://github.com/GomuGomuNo01/Simple-Banking-System-Python)

Une néobanque simulée veut savoir si ses partenaires commerciaux lui amènent de bons clients. Sur 18 mois d'activité (1 800 clients, 254 000 opérations), l'analyse montre que ces clients activent leur compte deux fois moins souvent que les autres (test du khi-deux à l'appui), d'où six recommandations priorisées.

`Python` `SQL` `Segmentation RFM` `Tests statistiques`

### [Telco Churn Prediction](https://github.com/GomuGomuNo01/telco-churn-prediction)

Une entreprise télécoms perd des clients chaque mois sans savoir lesquels cibler en priorité. Neuf modèles de machine learning sont comparés sur 7 043 clients, et celui retenu (Naive Bayes) détecte 73 % des résiliations réelles, un choix assumé au détriment de l'accuracy brute.

`Python` `scikit-learn` `Machine Learning`

### [Chatbot RAG · DocAssist](https://github.com/GomuGomuNo01/Chatbot-RAG)

Retrouver une information dans des documents internes prend du temps et le résultat n'est pas toujours fiable. Cet assistant IA cherche la réponse dans les documents, cite systématiquement sa source, et refuse de répondre plutôt que d'inventer quand l'information est absente.

`Python` `LangChain` `FAISS` `FastAPI`

### [Career-Ops](https://github.com/GomuGomuNo01/career-ops)

Candidater à de nombreuses offres en gardant chaque dossier pertinent prend du temps. Cet agent, construit sur Claude Code, analyse une offre, génère les documents de candidature correspondants et met à jour un tableau de suivi, via 14 modes spécialisés et des serveurs MCP connectés à des outils maison.

`Claude Code` `MCP` `Python` `Go`

---

## Projets Développement (le socle qui explique ma lecture de la donnée)

### [Hotel Management System](https://github.com/GomuGomuNo01/hotel-management-system)

Gère l'intégralité du cycle de vie d'un hôtel : réservations sans conflit de dates, paiements mobiles (Orange Money, Wave), arrivées, départs, ménage et réclamations. L'API Laravel et le frontend React communiquent en temps réel via WebSocket, pour que chaque mise à jour soit visible instantanément.

`Laravel` `React` `MySQL` `WebSocket`

### [Sales Report Automation](https://github.com/GomuGomuNo01/sales-report-automation)

Mettre en forme un rapport commercial à la main prend des heures et laisse place à l'erreur. Ce pipeline lit un export CSV brut, le nettoie, calcule les indicateurs clés et produit un PDF de 6 pages en 7 secondes, avec plus de 50 tests automatisés pour garantir sa fiabilité.

`Python` `pandas` `reportlab` `pytest`

### [Automatisation de Processus](https://github.com/GomuGomuNo01/automatisation-de-processus)

Six tâches manuelles (suivi de stock, envoi d'e-mails, collecte de données web) mobilisaient du temps chaque semaine. Ces scripts Python les exécutent seuls, d'abord en mode TEST puis en PRODUCTION, et sont en service depuis deux ans.

`Python` `Selenium` `Playwright` `openpyxl`

### [API REST JWT · Spring Boot](https://github.com/GomuGomuNo01/api-rest-jwt)

Une API doit être sécurisée sans devenir difficile à maintenir. Celle-ci authentifie chaque utilisateur par JWT et gère les droits par rôle, dans une architecture en couches (Controller / Service / Repository) couverte par des tests JUnit et documentée avec Swagger.

`Java` `Spring Boot` `Spring Security` `JUnit`

### [Mini-CRM](https://github.com/GomuGomuNo01/mini_crm)

Centralise le suivi des clients et des contrats d'une entreprise, plutôt que de les disperser entre tableurs et e-mails. L'application web (ASP.NET Core, Entity Framework Core) restitue les indicateurs clés dans un tableau de bord et s'appuie sur MySQL pour la persistance des données.

`C#` `ASP.NET Core 8` `EF Core` `MySQL`

### [Hospital](https://github.com/GomuGomuNo01/Hospital)

Les données de santé exigent un accès strictement contrôlé. Ce système sépare les droits en trois rôles (administrateur, médecin, infirmier), impose une authentification à deux facteurs et enregistre chaque action dans un journal d'audit inaltérable.

`Laravel` `PHP` `Blade` `MySQL`

---

## Stack technique

**Data & Analyse**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=flat-square&logo=apachespark&logoColor=white)

SQL avancé (CTE, fonctions de fenêtrage, vues analytiques) · DAX et modélisation en étoile · statistiques appliquées (test du khi-deux, segmentation RFM, VIF) · nettoyage, structuration et contrôle qualité de données

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
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
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

<div align="center">

![Stats GitHub](https://github-readme-stats.vercel.app/api?username=GomuGomuNo01&show_icons=true&theme=dark&hide_border=true&count_private=true)
![Langages les plus utilisés](https://github-readme-stats.vercel.app/api/top-langs/?username=GomuGomuNo01&layout=compact&theme=dark&hide_border=true)

</div>
