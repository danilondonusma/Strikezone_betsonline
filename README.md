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
**🧠 Business Questions and Insights Triggered:**

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

### 3. "Resultado Exacto" and "Ambos Anotan": Complex Markets Attract Sharp Bettors

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

### 4. La Liga vs. Liga BetPlay: Why Does an International League Generate Higher Winnings?

This is the **most critical finding** in this dashboard. Let's break down the competing hypotheses:

| Hypothesis | Explanation | Strategic Implication |
| :--- | :--- | :--- |
| **Information Asymmetry** | International leagues (La Liga, Premier League) have **vastly more public information** (player stats, team form, media coverage) available to bettors. Bettors can make more informed, data-driven decisions, reducing the house edge. | The house may lack the analytical tools to price odds accurately in international markets. |
| **Fan Base & Emotional Betting** | Real Madrid, Barcelona, and other international clubs have **massive global fan bases**. Colombian bettors may wager based on **loyalty and emotion** rather than statistical analysis, creating a "public bias" where the house is consistently on the wrong side of the bet. | This creates a **systemic risk** — the house is effectively subsidizing fan loyalty. |
| **Local Market Efficiency** | Liga BetPlay (Colombian league) has **less public information**, fewer analysts, and less media coverage. This creates **inefficiencies** that the house can exploit by setting odds that are more favorable to the platform. | The house may have a **local knowledge advantage** in Liga BetPlay, giving them a natural edge. |
| **Regulatory & Competition Factors** | Internacional markets are more competitive, with better odds offered by international bookmakers. To compete, StrikeZone may be offering more generous odds, reducing the house edge. | The platform may be overcompensating to attract users who would otherwise bet with international platforms. |


### 5. La Liga vs. Premier League: A Critical Distinction

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

### 6. Liga BetPlay: Why is it the most profitable competition?

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

The database follows a **normalized relational model** with the following core tables:

| Table | Description |
| :--- | :--- |
| `USUARIO` | Customer master data (KYC, demographics, registration) |
| `SALDO_CUENTA` | Account balances for each user |
| `METODO_PAGO` | Payment methods (Credit Card, Debit, Transfer, Digital Wallet) |
| `EVENTO` | Sports events with deporte, liga, fecha, and resultado |
| `PARTICIPANTES` | Athletes, teams, and fighters |
| `MERCADO` | Betting markets (Winner, Handicap, Total Anotaciones, etc.) |
| `APUESTA` | User bets with amounts, status, and timestamps |
| `CUOTA` | Odds for each bet at the time of placement |
| `HISTORIAL_CUOTA` | Historical odds changes (1-5 changes per bet) |
| `TRANSACCION` | Financial transactions (deposits, withdrawals, bets, winnings) |
| `HISTORIAL_APUESTA` | Audit log for bet changes |

**ER Diagram:** <img width="767" height="833" alt="image" src="https://github.com/user-attachments/assets/78ceacc5-109f-45de-ae4b-cb50a4cb0ca1" />

---

## 📁 Project Structure

Strikezone/

├── .env # Environment variables (credentials)

├── requirements.txt # Python dependencies

├── run.py # Entry point

├── apuestas_d.ipynb # Original exploratory notebook (legacy)

├── seeder/ # Main package

 │ ├── config.py # Database connection

 │ ├── main.py # Orchestrator

 │ ├── utils/

   │ │ └── helpers.py # Master data & helper functions

 │ └── seeders/

   │ ├── users.py # User, balance, payment method seeders

   │ ├── events.py # Events, participants, markets

   │ ├── bets.py # Bets, odds, odds history

   │ └── transactions.py # Financial transactions

└── dashboards/

└── strikezone.pbix # Power BI file


---

## 🧠 Key Design Decisions

Several architectural decisions were made to ensure data integrity, performance, and scalability:

### Database Design

| Decision | Implementation | Rationale |
| :--- | :--- | :--- |
| **Normalization** | 3NF (Third Normal Form) with 12 tables. | Minimizes redundancy and ensures data consistency across the platform. |
| **Referential Integrity** | Cascading foreign keys (`ON DELETE CASCADE`, `ON UPDATE CASCADE`). | Ensures that related records (e.g., bets, transactions) are automatically cleaned up when a user or event is removed. |
| **Triggers** | Automatic balance update after each transaction. | Prevents manual errors and ensures real-time balance accuracy. |
| **Indexes** | Optimized indexes on `ID_Usuario`, `ID_Evento`, `Fecha_hora`, and `Tipo_transaccion`. | Improves query performance for user lookups, event filtering, and financial reporting. |
| **Audit Trail** | `HISTORIAL_APUESTA` table tracks all bet status changes. | Enables fraud detection, user behavior analysis, and compliance with regulatory requirements. |
| **Currency Precision** | All monetary values stored as `DECIMAL(15,2)`. | Avoids floating-point precision errors common with `FLOAT` in financial calculations. |

### Python Architecture

| Decision | Implementation | Rationale |
| :--- | :--- | :--- |
| **Modular Design** | Separate modules for users, events, bets, and transactions. | Improves maintainability, testability, and scalability. |
| **Environment Variables** | Credentials stored in `.env` (not hardcoded). | Follows security best practices and prevents credential exposure on GitHub. |
| **Reusable Helpers** | Centralized master data and helper functions in `helpers.py`. | Eliminates code duplication and ensures consistency across seeders. |
| **Reproducibility** | `random.seed(42)` ensures consistent data generation. | Allows for reproducible testing and debugging. |

### Power BI Design

| Decision | Implementation | Rationale |
| :--- | :--- | :--- |
| **Star Schema** | Fact tables (`APUESTA`, `TRANSACCION`) connected to dimension tables (`USUARIO`, `EVENTO`, `MERCADO`). | Optimizes DAX performance and simplifies report creation. |
| **DAX Measures** | Key metrics (GGR, ARP User, Win Rate) implemented as measures. | Enables dynamic filtering and drill-through without recalculating base data. |
| **Drill-Through** | Users can click from summary views to detailed user-level data. | Enables root-cause analysis for business anomalies. |

---
## 📊 Data Seeding

The Python notebook generates realistic synthetic data for all tables using the **Faker** library with Colombian locale (`es_CO`). This approach enables the platform to test and validate the data pipeline before deploying with real data.

### Data Volume Generated

| Entity | Quantity | Description |
| :--- | :--- | :--- |
| **Users** | 300 | Includes KYC status, gender, city, registration date, and age distribution. |
| **Sports Events** | 60 | Across 5 sports (Football, Basketball, Tennis, MMA, Cycling) and 12 leagues. |
| **Bets** | 500 | Realistic COP amounts with sport-consistent participants and status distribution. |
| **Financial Transactions** | 5,000 | Deposits, withdrawals, bet placements, winnings, and adjustments. |
| **Odds History** | ~1,500 | Simulated 1-5 odds changes per bet to reflect market dynamics. |

### Key Seeding Features

| Feature | Implementation | Why it matters |
| :--- | :--- | :--- |
| **User Profile Distribution** | KYC status weighted (70% verified, 20% pending, 10% rejected). | Reflects real-world verification rates and enables segmentation analysis. |
| **Gender Distribution** | 62% male, 35% female, 3% other (based on Colombian market data). | Enables gender-based behavioral analysis. |
| **Bet Amount Distribution** | Weighted by user profile (30% casual, 45% frequent, 20% high-value, 5% whale). | Simulates realistic betting behavior across different user segments. |
| **Participant Consistency** | Event participants are matched to the sport (e.g., football teams for football events). | Ensures data consistency and enables sport-specific analysis. |
| **Balance Validation** | Solvency check before recording withdrawals or bet transactions. | Prevents negative balances and simulates real-world financial controls. |
| **Reproducibility** | Fixed random seed (`random.seed(42)`). | Enables identical data generation across multiple runs for testing. |

### Data Generation Process

The seeding process follows a **dependency-aware order** to maintain referential integrity:

1. **Users** → **Saldos** → **Métodos de Pago**
2. **Participantes** → **Eventos** → **Mercados** → **Participante_Evento**
3. **Apuestas** → **Cuotas** → **Historial_Cuota**
4. **Transacciones** (validates user balance before processing)

This ensures that all foreign key constraints are satisfied before inserting dependent records.

---

## ⚙️ Setup & Installation

1. **Clone the repository:**
   ```bash 
   git clone https://github.com/danilondonusma/Strikezone_betsonline.git
   cd Strikezone_betsonline bash 
   
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Set up your MySQL database:**

- Ensure MySQL 8.0 is running.
- Create a database named apuestas_d.
- Run the schema script from the repository (if provided).

5. **Configure environment variables:**

- Copy .env.example to .env.
- Edit .env with your MySQL credentials:
   ```bash
   DB_HOST=localhost
   DB_PORT=3306
   DB_USER=your_user
   DB_PASSWORD=your_password
   DB_NAME=apuestas_d

6. **Run the data seeder:**
   ```bash
   python run.py

7. **Open the Power BI dashboard:**

- Open dashboards/strikezone.pbix.
- Update the data source connection if needed.
  
---

## 💡 Key Insights & Business Recommendations

This section synthesizes the most critical findings from the three dashboards and translates them into actionable business strategies. The recommendations are prioritized based on **financial impact**, **strategic relevance**, and **ease of implementation**.

---

### 🔍 Top 5 Strategic Insights

#### 1. The Platform Is Operating at a Significant Loss

- **Total wagered:** COP 321.75M
- **Total paid out:** COP 671.70M
- **Net margin:** **-COP 349.95M** (-109% margin)

**Interpretation:** The house is paying out **more than double** what it receives in wagers. This is a **critical red flag** that the current business model is not viable. The platform is effectively subsidizing user winnings without a sustainable revenue model.

**Priority:** 🔴 **Critical** — Immediate action required.

---

#### 2. Average Bet Ticket Is 50x Above Market Average

- **StrikeZone average bet:** COP 2.51M
- **Colombian market average:** COP 50,000

**Interpretation:** This indicates a **concentration of high-value bettors** (potential "Sharp Bettors") who place large, well-informed wagers. While this could be a competitive advantage, it also represents a **concentration risk** — if these users continue to win consistently, the losses will compound.

**Priority:** 🟠 **High** — Validate data and develop a premium strategy.

---

#### 3. Football Drives High Volume but High Losses

- Football accounts for **45% of all bets**.
- Football also generates the **highest losses for the house**.

**Interpretation:** The platform is **overexposed** to football markets. While football is the most popular sport, the house is consistently losing on these bets. This suggests that odds may be **too generous** or that the platform is attracting **Sharp Bettors** in this market.

**Priority:** 🟠 **High** — Recalibrate odds and diversify risk.

---

#### 4. La Liga Generates High User Winnings — Premier League Does Not

- **La Liga** and **Vuelta a España** generate the highest user winnings.
- **Premier League** does **not** generate significant losses.

**Interpretation:** The initial hypothesis of "international vs. local" is **too simplistic**. La Liga's losses are likely driven by a **combination of cultural affinity** (Spanish language, media coverage) and a **concentration of Sharp Bettors** who specialize in Spanish football. The Premier League, despite being international, does not attract the same level of informed betting.

**Priority:** 🟡 **Medium** — Conduct a league-specific profitability analysis.

---

#### 5. Liga BetPlay Is the Only Profitable Competition

- Liga BetPlay is the **only competition** where the house maintains a **positive edge**.

**Interpretation:** Unlike La Liga, Liga BetPlay attracts **recreational bettors** who bet based on **emotional loyalty** to local teams, rather than advanced analytics. This creates a **natural house advantage** — bettors overestimate their teams, and the house profits from this bias.

**Priority:** 🟢 **High** — Double down on Liga BetPlay.

---

### 💼 Strategic Recommendations

Based on these insights, the following **five strategic recommendations** are prioritized for implementation:

#### 1. 🚨 Immediate Odds Recalibration (Financial Recovery)

**Action:**
- Conduct a comprehensive review of all odds across all sports and markets.
- Adjust odds to achieve a **minimum house edge of 5%** (from the current negative margin).
- Introduce **dynamic odds adjustment** for high-volume markets (football, La Liga).

**Expected Impact:**
- Stabilize the platform's financial position within 3 months.
- Reduce losses by an estimated **30-40%** in the first quarter.

**Priority:** 🔴 **Critical**

---

#### 2. 🎯 Launch "StrikeZone Pro" Premium Tier (User Segmentation)

**Action:**
- Develop a segmentation model to classify users based on behavior (bet size, market selection, frequency, win rate).
- Identify **Sharp Bettors** and create a **"StrikeZone Pro" premium tier** offering exclusive benefits (better odds, cashback, personalized insights).
- For **recreational bettors**, develop educational content to improve retention.

**Expected Impact:**
- Monetize high-value users while limiting risk exposure.
- Increase user lifetime value (LTV) by **20-30%** .

**Priority:** 🟠 **High**

---

#### 3. ⚽ Expand Liga BetPlay Offerings (Profitability Growth)

**Action:**
- Double the number of betting markets available for Liga BetPlay matches (e.g., "First Goalscorer", "Half-Time/Full-Time", "Both Teams to Score").
- Launch a **"Colombian Football Boost"** campaign with promotions tied exclusively to local competitions.

**Expected Impact:**
- Increase GGR from Liga BetPlay by **40-50%** within 6 months.
- Establish a **competitive moat** in the Colombian market.

**Priority:** 🟢 **High**

---

#### 4. 🧠 Conduct a Market Efficiency Study (Data-Driven Odds Calibration)

**Action:**
- Benchmark StrikeZone's odds against **5-10 international competitors** (Bet365, Betfair, 1xBet) for the top 10 markets.
- Identify overpriced and underpriced markets and recalibrate accordingly.
- Implement a **machine learning model** to predict optimal odds based on historical data, public sentiment, and betting volume.

**Expected Impact:**
- Improve odds accuracy and reduce losses in high-risk markets.
- Increase overall house edge by **2-3%** across all markets.

**Priority:** 🟡 **Medium**

---

#### 5. 📊 Develop a "Sharp Bettor Monitoring System" (Risk Management)

**Action:**
- Implement **real-time monitoring** of individual user behavior.
- Flag users with **consistent winning patterns** and automatically adjust their access to high-risk markets.
- Introduce **maximum payout limits** for high-risk markets to limit exposure.

**Expected Impact:**
- Reduce exposure to Sharp Bettors by **20-25%** .
- Protect the platform's financial stability without alienating recreational users.

**Priority:** 🟡 **Medium**

---

### 📋 Executive Summary (For CEO / Stakeholders)

| Metric | Current State | Recommended Target | Action Owner |
| :--- | :--- | :--- | :--- |
| **Net Margin** | -109% | +5% | Head of Trading / Risk |
| **Average Bet Ticket** | COP 2.51M | COP 500K (validate first) | Head of Data |
| **La Liga Loss Ratio** | High (losses) | Reduce by 20% | Head of Trading |
| **Liga BetPlay Margin** | Positive (profitable) | Increase by 40% | Head of Marketing |
| **Football Loss Ratio** | 60%+ | <50% | Head of Trading |

---

### 🚀 Next Steps (Q1 Roadmap)

| Quarter | Milestone | Owner |
| :--- | :--- | :--- |
| **Q1 Month 1** | Odds recalibration across all markets | Head of Trading |
| **Q1 Month 2** | Launch "StrikeZone Pro" premium tier | Head of Product |
| **Q1 Month 3** | Market Efficiency Study completed | Head of Data |
| **Q1 Month 3** | Liga BetPlay expansion campaign launched | Head of Marketing |

---

### 📌 Conclusion

StrikeZone has a **strong product foundation** and a **unique user base** with high-value potential. However, the current financial performance is **unsustainable**. By implementing the recommendations above, the platform can:

1. **Stabilize its financial position** within 3 months.
2. **Monetize its high-value user base** through segmentation.
3. **Expand its most profitable market** (Liga BetPlay).
4. **Build a data-driven competitive advantage** through advanced odds calibration and risk management.

**The path to profitability is clear — now it's time to execute.**


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
