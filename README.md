# StrikeZone — Sports Betting Platform 
## Database & Analytics Project

End-to-end data project for a fictional Colombian online sports betting platform: relational database design, Python data seeding, and business intelligence dashboards.


## Project Overview

StrikeZone is a simulated online sports betting platform designed as an academic and portfolio project. The goal was to build a complete data pipeline, from relational database schema to business analysis, replicating the structure and logic of a real-world betting operation in the Colombian market.

## The project covers three layers:

- Data modeling — relational schema designed in MySQL
  
- Data generation — realistic synthetic data seeded with Python
  
- Business analysis — descriptive dashboards built in Power BI


# Business Context
The Colombian online sports betting market is one of the most dynamic in Latin America. In this context, StrikeZone positions itself as a premium platform targeting high-value users with above-average bets, and seeks to differentiate itself through data-driven business solutions. This project simulates betting market data—standardized, optimized, and analyzed using tools such as Python and MySQL—and answers key business questions related to user behavior, financial results, and market activity.

## Tech Stack
- Layer Tool Relational 
- DatabaseMySQL 8.0
- Data SeedingPython 3.13 · Faker · mysql-connectorBusiness Intelligence
- Power BI DesktopVersion 
- ControlGit / GitHub

## Repository Structure

strikezone/

│
├── schema/
│   └── apuestas_d.sql          # Full database schema with tables, indexes and triggers

│
├── seeder/
│   └── apuestas_d.ipynb        # Python notebook for synthetic data generation

│
├── dashboards/
│   └── strikezone.pbix         # Power BI file with three analytical dashboards

│   └── img/
│       ├── dashboard_clientes.png
│       ├── dashboard_apuestas.png
│       └── dashboard_mercado.png

│
└── README.md

## Database Schema
The schema models the core entities of a sports betting operation:

USUARIO — registered users with KYC status, city and demographic data.

SALDO_CUENTA — user account balances, updated automatically via triggers.

METODO_PAGO — payment methods per user.

EVENTO — sporting events across 5 sports and 12 leagues.

MERCADO — betting markets per event (Winner, Handicap, Both Score, etc.).

PARTICIPANTES — teams and athletes linked to events.

APUESTA — individual bets with amount, status and odds.

CUOTA — odds snapshot at the time of each bet.

TRANSACCION — full financial transaction log.

HISTORIAL_CUOTA — odds movement history per market.

HISTORIAL_APUESTA — automated bet audit trail.

#### Key design decisions:

- Triggers ensure automatic balance updates on every transaction.
- Indexes optimized for user queries, event filtering and odds history
- Referential integrity enforced with cascading foreign keys


# Data Seeding
The Python notebook generates realistic synthetic data for all tables using the Faker library with Colombian locale (es_CO).

Data volume generated:

- 300 users with KYC status, gender, city and registration date
- 60 sporting events across 5 sports and 12 leagues
- 500 bets with realistic COP amounts and sport-consistent participants
- 5,000 financial transactions with balance validation
- Full odds change history per bet

#### Key seeding features:

- Bet amounts distributed by realistic user profiles (casual, frequent, high-value)
- KYC status weighted to reflect real-world verification rates (70% verified)
- Gender distribution based on Colombian market data
- Solvency check before recording withdrawal or bet transactions

Setup:

1. bashpip install mysql-connector-python faker
2. Update the connection config in the notebook before running:

pythonDB_CONFIG = {

    'host':     'localhost',
    'port':     3306,
    'user':     'root',
    'password': 'your_password_here',
    'database': 'apuestas_d'
}

Then run all cells sequentially. The reset_db() function clears all tables before each run.


# Dashboards & Key Findings
Three Power BI dashboards answer the descriptive business questions defined for this project. Screenshots below — the .pbix file is available in the dashboards/ folder.

### 1.  Customer Profile Dashboard

<img width="1292" height="708" alt="Tab usuarios" src="https://github.com/user-attachments/assets/3faa8db9-a90a-4fa4-a42f-8e9e28a4cf2e" />

- 87 verified users · 128 total bets
- Dominant age segment: 55+ (92 users) — consistent with high-value bettor profile.
- Gender split: 61% male / 36% female — female participation significantly above market average (~10%).
- Top cities: Cartagena, Manizales, Barranquilla.
- Payment methods evenly distributed across all 5 types.

### 2. Financial Performance Dashboard
<img width="1300" height="724" alt="image" src="https://github.com/user-attachments/assets/f5a6b212-66ae-4c6c-8680-2d094b8932da" />

- Total wagered: COP 321.75M · Total paid out: COP 671.70M.
- Net margin: -COP 349.95M means platform operating at a loss.
- Average bet ticket: COP 2.51M — 50x above the Colombian market average of COP 50,000.
- Football drives the highest volume but also the highest losses for the house.
- Liga BetPlay is the only competition where the house maintains a positive edge.

### 3. Market & Events Dashboard
<img width="1286" height="713" alt="image" src="https://github.com/user-attachments/assets/2766b3e6-f9f7-4b51-a63c-5e372fed8b63" />

- Resultado Exacto and Ambos Anotan concentrate the highest wagered volume.
- Market type distribution is nearly uniform across all 5 types (~20% each).
- La Liga and Vuelta a España generate the highest user winnings — highest risk markets for the platform.


### 💡 Business Insights & Recommendations

- Odds recalibration is urgent, because a net margin of 349M indicates cuotas are not generating sufficient house edge.
- Diversify user base toward recreational bettors current high-ticket users are sophisticated and win consistently.
- Capitalize on Liga BetPlay is the only market where the house has a natural edge.
- Leverage female segment of 36% female participation is a competitive differentiator worth developing.
- Implement AI-powered odds engine — dynamic odds adjustment and user segmentation are the long-term solution to margin recovery.


### ⚠️ Limitations

All data is synthetically generated with random distributions, findings are illustrative, not representative of real market behavior
Bet volume per user is low due to dataset size constraints
Age distribution reflects random seeding, not a real acquisition campaign


# 👩‍💻 Authors

### Daniela Londoño Usma
Political Scientist & Data Analyst,
Medellín, Colombia


### Dayana López 
Engineer & Data Analyst,
Córdoba, Colombia



### Andrés García Sosa
Engineer & Data Analyst,
Cucuta, Colombia
