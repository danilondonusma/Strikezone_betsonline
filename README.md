# ⚽ StrikeZone - Sports Betting Analytics Platform

![MySQL](https://img.shields.io/badge/MySQL-8.0-blue?logo=mysql)
![Python](https://img.shields.io/badge/Python-3.9+-green?logo=python)
![PowerBI](https://img.shields.io/badge/PowerBI-F2C811?logo=powerbi&logoColor=black)
![Faker](https://img.shields.io/badge/Faker-18.0+-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A complete **end-to-end data analytics project** for a simulated sports betting platform operating in the Colombian market. From database modeling with MySQL, synthetic data generation with Python, to executive dashboards in Power BI — this project demonstrates the full lifecycle of a data pipeline designed to answer real business questions.

## 📋 Table of Contents

1. [Business Context & Problem Statement](#business-context--problem-statement)
2. [Key Business Questions Answered](#key-business-questions-answered)
3. [Tech Stack](#tech-stack)
4. [Dashboard Highlights](#dashboard-highlights)
5. [Database Schema](#database-schema)
6. [Project Structure](#project-structure)
7. [Setup & Installation](#setup--installation)
8. [Key Insights & Business Recommendations](#key-insights--business-recommendations)
9. [Next Steps](#next-steps)
10. [License](#license)

## 📌 Business Context & Problem Statement

The Colombian online sports betting market is one of the most dynamic in Latin America. In this context, StrikeZone is a **simulated sports betting platform** that positions itself as a premium platform targeting high-value users with above-average bets, and seeks to differentiate itself through data-driven business solutions. The business offers betting markets on five sports: Football, Basketball, Tennis, MMA, and Cycling.

**The Problem:**  
The company lacks a centralized data infrastructure to understand user behavior, betting patterns, financial performance and guarantee compliance with responsible gaming regulations . Without this visibility, they cannot:
- Identify high-value customer segments.
- Optimize betting market offerings.
- Detect fraud or anomalous patterns.
- Make data-driven decisions about marketing and operations.

**The Solution:**  
This project designs and implements a complete data pipeline — from a normalized relational database to interactive dashboards — that transforms raw transactional data into actionable business intelligence.

## ❓ Key Business Questions Answered

**[NEW]**  
The dashboards answer these 8 strategic questions:

1. **Which user segments (casual, frequent, high-value) generate the most revenue?**
2. **What is the Gross Gaming Revenue (GGR) by month and sport?**
3. **Which sports and betting markets attract the highest betting volume?**
4. **What are the most popular payment methods among users?**
5. **How does user activity vary by city and region in Colombia?**
6. **What is the average bet size and how does it vary by user segment?**
7. **What is the KYC verification rate and how does it impact betting behavior?**
8. **Which users are at risk of churn based on recent activity?**

---

## 🛠️ Tech Stack


| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Database** | MySQL 8.0 | Relational data modeling, referential integrity, triggers, and indexes |
| **Data Generation** | Python 3.9+ with Faker | Synthetic data generation with realistic distributions (KYC, gender, bet sizes) |
| **Data Processing** | Python (pandas, mysql-connector) | Data validation, cleaning, and loading |
| **Visualization** | Power BI | Interactive dashboards with DAX measures and drill-through capabilities |
| **Environment** | python-dotenv | Secure credential management |

## 📊 Dashboard Highlights

The next three Power BI dashboards answer the descriptive business questions defined for this project. Screenshots below — the .pbix file is available in the dashboards/ folder.

### 1.  Customer Profile Dashboard

<img width="1292" height="708" alt="Tab usuarios" src="https://github.com/user-attachments/assets/3faa8db9-a90a-4fa4-a42f-8e9e28a4cf2e" />

- 87 verified users · 128 total bets
- Dominant age segment: 55+ (92 users) — consistent with high-value bettor profile.
- Gender split: 61% male / 36% female — female participation significantly above market average (~10%).
- Top cities: Cartagena, Manizales, Barranquilla.
- Payment methods evenly distributed across all 5 types.

**🧠 Business Questions Triggered:**

The geographic distribution reveals an **anomalous pattern** compared to industry benchmarks. Colombia's three largest cities — Bogotá, Medellín, and Cali — account for over 60% of the country's GDP and population, yet they are **underrepresented** in StrikeZone's user base compared to smaller cities like Cartagena, Manizales, and Barranquilla.

This raises critical strategic questions:
- **Is this a market opportunity or a strategic misfit?**
  - *Opportunity:* The platform may be under-penetrated in major cities, suggesting a massive growth opportunity through targeted marketing campaigns in Bogotá, Medellín, and Cali.
  - *Misfit:* The platform's offerings (sports, markets, odds) may appeal more to regional audiences, requiring a product strategy adjustment.

- **Is there a correlation between city size and betting behavior?**
  - Users in smaller cities may have stronger community ties, higher loyalty, and lower churn rates. This could inform a "community-first" marketing strategy.

- **Are we missing a demographic segment in large cities?**
  - The high female participation (36% vs. 10% industry average) is a competitive advantage. Could this be leveraged in marketing campaigns targeting women in Bogotá and Medellín?

**Next Step:** A deeper cohort analysis by city and age segment is recommended to validate whether these patterns are statistically significant or driven by sample size.

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
