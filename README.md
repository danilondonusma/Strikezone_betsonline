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
**Key Metrics:**

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

**Key Metrics:**
- **Total wagered:** COP 321.75M
- **Total paid out:** COP 671.70M
- **Net margin:** **-COP 349.95M** (platform operating at a significant loss)
- **Football drives the highest volume** but also the highest losses for the house.

---
**🧠 Business Questions Triggered:**

The financial metrics reveal a **critical profitability crisis** that demands immediate strategic intervention. Let's break down the three most pressing issues:

### 1. Net Margin: -COP 349.95M

This is the **most alarming KPI** in the entire dashboard. The platform is paying out **more than double** what it receives in wagers (671.70M vs. 321.75M), resulting in a **-109% net margin**.

**Potential Root Causes:**
- **Overly generous odds:** The house may be offering odds that are too favorable to users, resulting in consistent losses.
- **Lack of risk management:** Markets may not be properly balanced (e.g., heavy betting on one side of a market without adjusting odds).
- **Competitive pressure:** The platform may be offering promotional odds (e.g., "money-back specials") that are not sustainable.
- **Data quality issues:** There may be errors in payout calculations or sample bias in the test data.

**Strategic Implications:**
- This is a **red flag** that the business model is not viable in its current form.
- Immediate action is required to **recalibrate odds** and implement **dynamic risk management**.
- The platform should consider **restricting high-risk markets** or introducing **maximum payout limits**.

### 2. Football Drives High Volume & High Losses

Football (Fútbol) generates the highest betting volume but also the **highest losses for the house**. This is consistent with the global sports betting industry, where football markets are highly competitive and often operate on thin margins.

**Strategic Questions:**
- **Are football odds too generous?** If the platform is consistently losing on football, odds may need to be adjusted downward (e.g., from 1.90 to 1.85) to improve the house edge.
- **Can we introduce new football markets?** Instead of competing on standard markets (Winner, Handicap), the platform could innovate with derivative markets (e.g., "First Goalscorer", "Half-Time/Full-Time", "Both Teams to Score") where the house has a natural edge.
- **Is there a correlation with user segment?** Do high-value users bet predominantly on football? If so, targeted promotions on other sports could diversify risk.

---
### 💼 Strategic Recommendations

Based on these findings, I recommend the following immediate actions:

1. **Odds Recalibration:** Conduct a comprehensive review of all odds across all sports and markets. Adjust odds to achieve a **minimum house edge of 5%** (from the current negative margin).

2. **Risk Management Implementation:** Introduce a **dynamic odds adjustment system** that automatically adjusts odds based on betting volume, market sentiment, and user segments.

3. **Data Validation:** Validate the synthetic data against real-world benchmarks to ensure the "average bet ticket" and "net margin" metrics are realistic and not artifacts of the data generation process.

4. **Football Market Innovation:** Introduce "micro-markets" (e.g., "Next Goalscorer", "Card Count", "Corner Count") in football to diversify risk and create new revenue streams.

---

### 📊 Key Performance Indicators to Monitor

| KPI | Current | Target | Action Plan |
| :--- | :--- | :--- | :--- |
| **Net Margin** | -109% | +5% | Recalibrate odds by 3-5% |
| **Average Bet Ticket** | COP 2.51M | COP 500K | Validate data; introduce premium tier |
| **Football Loss Ratio** | 60%+ | <50% | Introduce micro-markets & adjust odds |
| **Liga BetPlay Margin** | Positive | Expand | Launch marketing campaigns |

### 3. Market & Events Dashboard
<img width="1286" height="713" alt="image" src="https://github.com/user-attachments/assets/2766b3e6-f9f7-4b51-a63c-5e372fed8b63" />

- **Average bet ticket:** **COP 2.51M** — 50x above the Colombian market average (COP 50,000)
- **Liga BetPlay is the only competition** where the house maintains a positive edge.
- **Resultado Exacto and Ambos Anotan concentrate the highest wagered volume**.
- **Market type distribution is nearly uniform across all 5 types (~20% each)**.
- **La Liga and Vuelta a España generate the highest user winnings — highest risk markets for the platform**.

**🧠 Business Questions Triggered:**

### 1. Average Bet Ticket: COP 2.51M

This is **50x higher than the Colombian market average** (COP 50,000). While this could indicate a high-value user segment, it also represents a **concentration risk**.

**Two Competing Hypotheses:**

| Hypothesis | Explanation | Strategic Implication |
| :--- | :--- | :--- |
| **Premium User Opportunity** | The platform has attracted a niche of high-net-worth bettors who place large wagers. | **Opportunity:** Develop a "Premium Betting" tier with personalized services, VIP odds, and dedicated account managers. |
| **Sample Bias** | The synthetic data may have generated disproportionately large bets due to unrealistic bet size ranges. | **Action:** Review and recalibrate the data generation logic to ensure realistic bet sizes. |

**Recommendation:** Validate this metric with real-world benchmarks. If the data is accurate, this is a **competitive advantage** that should be leveraged with a premium user strategy.

---

### 2. Liga BetPlay: The Only Profitable Competition

Liga BetPlay (the Colombian football league) is the **only competition** where the house maintains a positive edge. This is a **bright spot** in an otherwise bleak financial picture.

**Insights & Action:**
- **Liga BetPlay may have less efficient odds** compared to international competitions (Premier League, Champions League), giving the house an information advantage.
- **Recommendation:** Double down on Liga BetPlay by offering more markets, promotions, and marketing campaigns tied to Colombian football.
- **Study the odds calibration** in Liga BetPlay and replicate it across other competitions.

### 3. "Resultado Exacto" and "Ambos Anotan" — Complex Markets Attract Sharp Bettors

These markets (Exact Score and Both Teams to Score) are among the most complex and carry the highest odds. Their high wagered volume suggests that a subset of StrikeZone users — potentially **"Sharp Bettors"** — prefer high-risk, high-reward markets.

**Why is this significant?**

| Bettor Type | Characteristics | Behavior |
| :--- | :--- | :--- |
| **Recreational Bettor** | Bets on favorites, low odds, familiar markets (Winner, Handicap). | Prefers "Winner" markets (40% of volume). |
| **Sharp Bettor** | Data-driven, seeks value, bets on complex markets, often wins. | Prefers "Resultado Exacto" and "Ambos Anotan" (higher odds, higher risk). |

**Strategic Implications:**
- The **near-uniform distribution** across all 5 market types (~20% each) is unusual. In most platforms, "Winner" markets dominate with 50-60% of volume.
- This suggests that StrikeZone has a **disproportionately high concentration of Sharp Bettors** compared to industry averages.
- **Action:** Develop a **"Sharp Bettor Identification" strategy** using behavioral analytics (e.g., bet size, market selection, frequency, win rate). Once identified, create a **"StrikeZone Pro" premium tier** with exclusive perks (better odds, cashback, personalized promotions).

### 4. La Liga vs. Liga BetPlay — Why Does an International League Generate Higher Winnings?

This is the **most critical finding** in this dashboard. Let's break down the competing hypotheses:

| Hypothesis | Explanation | Strategic Implication |
| :--- | :--- | :--- |
| **Information Asymmetry** | International leagues (La Liga, Premier League) have **vastly more public information** (player stats, team form, media coverage) available to bettors. Bettors can make more informed, data-driven decisions, reducing the house edge. | The house may lack the analytical tools to price odds accurately in international markets. |
| **Fan Base & Emotional Betting** | Real Madrid, Barcelona, and other international clubs have **massive global fan bases**. Colombian bettors may wager based on **loyalty and emotion** rather than statistical analysis, creating a "public bias" where the house is consistently on the wrong side of the bet. | This creates a **systemic risk** — the house is effectively subsidizing fan loyalty. |
| **Local Market Efficiency** | Liga BetPlay (Colombian league) has **less public information**, fewer analysts, and less media coverage. This creates **inefficiencies** that the house can exploit by setting odds that are more favorable to the platform. | The house may have a **local knowledge advantage** in Liga BetPlay, giving them a natural edge. |
| **Regulatory & Competition Factors** | Internacional markets are more competitive, with better odds offered by international bookmakers. To compete, StrikeZone may be offering more generous odds, reducing the house edge. | The platform may be overcompensating to attract users who would otherwise bet with international platforms. |


### 5. La Liga vs. Premier League — A Critical Distinction

**Key Finding:** La Liga and Vuelta a España generate **high user winnings**, while the **Premier League does NOT** — despite both being international competitions.

**Why does La Liga attract Sharp Bettors while the Premier League does not?**

| Factor | La Liga | Premier League | Explanation |
| :--- | :--- | :--- | :--- |
| **Cultural & Linguistic Connection** | 🇪🇸 Spanish language and culture are deeply embedded in Colombian media and daily life. | 🇬🇧 Language barrier (English) and cultural distance reduce emotional connection. | Colombian bettors have **more information and emotional investment** in Spanish football than English football. |
| **Media Coverage** | La Liga matches are broadcast with Spanish commentary at favorable times (morning/afternoon). | Premier League matches are broadcast in English or with Spanish commentary at less favorable times (early morning/late night). | Higher exposure drives more informed bets — leading to higher user winnings. |
| **Sharp Bettor Specialization** | Sharp bettors may specialize in leagues with **more available public data** — La Liga has extensive analytics (Opta, StatsBomb) in Spanish. | Premier League also has data, but the language barrier may reduce accessibility for some bettors. | Sharp bettors in Colombia may gravitate toward La Liga due to lower friction in accessing information. |
| **Concentration of High-Value Users** | A small but highly active segment may be placing **large, well-informed bets** on La Liga. | Premier League bets may be more distributed across recreational users. | If a few Sharp users win consistently, they can significantly impact house profitability. |

**Conclusion:** The "International League" hypothesis is **too simplistic**. La Liga's outsized losses for the house are likely driven by a **combination of cultural affinity, media accessibility, and a concentration of Sharp bettors** — factors that do not apply equally to the Premier League.

**Recommendation:** Conduct a **"League Profitability Analysis"** to identify which specific factors (bet size, user segment, market type) are driving La Liga's losses. This will inform more targeted risk management strategies.

### 6. Liga BetPlay — Why is it the most profitable competition?

While La Liga and Vuelta a España generate significant losses for the house, **Liga BetPlay consistently delivers positive margins**. 

#### The  Reasons:

| Factor | Explanation | Evidence |
| :--- | :--- | :--- |
| **1. Recreational vs. Sharp Bettors** | Liga BetPlay attracts **recreational bettors** who wager based on **emotional loyalty** to local teams (Millonarios, Atlético Nacional, Junior) rather than statistical analysis. | This "home bias" creates predictable patterns that the house can exploit — bettors overestimate their teams, creating value for the platform. |
| **2. Distributed Betting Volume** | Bets on Liga BetPlay are **spread across a large number of users** with small to medium bet sizes. | This **dilutes risk** — no single user or bet can significantly impact the house's overall P&L. |
| **3. Lower Access to Advanced Analytics** | While media coverage is extensive, **advanced data** (xG, heat maps, predictive models) is **less accessible** for Liga BetPlay compared to La Liga or the Premier League. | The average bettor lacks the analytical tools to make fully informed bets, giving the house a **natural information advantage**. |
| **4. Less Competitive Odds** | International bookmakers (Bet365, Betfair) **do not invest heavily** in pricing Liga BetPlay odds, reducing competitive pressure. | StrikeZone can offer **slightly less favorable odds** without losing users to competitors, improving the house edge. |
| **5. Emotional "Chasing" Behavior** | Colombian bettors often **"chase"** their losses after a team defeat, placing additional bets to recover losses. | This behavior increases betting volume and the house's overall margin, especially in local derbies. |


### 💼 Strategic Recommendations

Based on these findings, I recommend the following actions:

1. **Sharp Bettor Identification Program**  
   - Develop a segmentation model to classify users based on behavior (bet size, market selection, frequency, win rate).  
   - Create a **"StrikeZone Pro"** premium tier for Sharp Bettors offering exclusive benefits (better odds, cashback, personalized insights).

2. **Market Efficiency Study**  
   - Benchmark StrikeZone's odds against 5-10 international competitors for the top 10 markets.  
   - Identify overpriced and underpriced markets and recalibrate to achieve a **minimum 5% house edge**.

3. **Expand Liga BetPlay Offerings**  
   - Double the number of markets available for Liga BetPlay matches.  
   - Run a "Colombian Football Boost" campaign with promotions tied exclusively to local competitions.

4. **Risk Management for International Leagues**  
   - Introduce **dynamic odds adjustment** for high-volume international markets (La Liga, Champions League).  
   - Consider **lowering maximum payouts** for high-risk markets to limit exposure.

5. **Data-Driven Odds Calibration**  
   - Implement a **machine learning model** to predict optimal odds based on historical data, public sentiment, and betting volume.

### 📊 Key Performance Indicators to Monitor

| KPI | Current | Target | Action Plan |
| :--- | :--- | :--- | :--- |
| **Liga BetPlay Margin** | Positive (profitable) | Maintain | Expand offerings & promotions |
| **La Liga Loss Ratio** | High (losses for the house) | Reduce by 20% | Recalibrate odds & introduce dynamic adjustments |
| **Resultado Exacto Volume** | High (complex markets) | Maintain / Grow | Launch "StrikeZone Pro" tier for Sharp Bettors |
| **Market Distribution** | Uniform (~20% each) | 35% Winner, 25% Handicap, 20% Complex | Use promotions to guide users toward profitable markets |

## 🗄️ Database Schema
<img width="767" height="833" alt="image" src="https://github.com/user-attachments/assets/78ceacc5-109f-45de-ae4b-cb50a4cb0ca1" />


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
