# Supply Chain & Sales Performance Analytics

## 📊 Project Overview

Analyzed 180K+ supply chain transaction records to evaluate delivery performance, shipping efficiency, sales trends, regional performance, and customer/category-level patterns.

The project combines **Python, SQL (DuckDB), and Power BI** to transform raw supply chain data into business-focused insights and an interactive analytics dashboard.

## 🎯 Business Objectives

- Measure overall delivery and cancellation performance
- Identify shipping modes with higher late-delivery rates
- Compare delivery performance across markets and regions
- Analyze scheduled vs. actual shipping duration
- Identify delay patterns across orders
- Evaluate sales performance by category and region
- Compare performance across customer segments
- Analyze profitability across product categories

## 🛠️ Tools & Technologies

- **Python** — data preparation, validation, KPI calculation
- **SQL / DuckDB** — analytical queries and aggregations
- **Power BI** — interactive dashboard and visualization
- **Git & GitHub** — version control and portfolio management

## 📈 Key Findings

- **180,519** total records analyzed
- **172,765** delivery records
- **7,754** cancelled records
- Overall delivery records showed a high late-delivery rate
- **First Class** had the highest late-delivery rate among shipping modes
- **Standard Class** handled the largest delivery volume
- Delivery performance was broadly consistent across major markets
- Shipping delays varied significantly based on scheduled shipping duration
- **Consumer** customers represented the largest sales segment
- **Fishing** generated the highest sales among the analyzed categories

## 📊 Power BI Dashboard

The dashboard provides an interactive view of:

- Total Orders
- Total Sales
- Late Delivery Rate
- Average Shipping Delay
- Late Delivery Rate by Shipping Mode
- Sales by Category
- Sales Trend Over Time
- Sales by Region
- Orders by Actual Shipping Days
- Profitability by Category
- Market-level filtering

## 📁 Project Structure

```text
supply-chain-delivery-analytics/
│
├── dashboard/
├── data/
│   ├── DataCoSupplyChainDataset.csv
│   └── DataCoSupplyChain_UTF8.csv
│
├── notebooks/
├── outputs/
│   ├── service_level_performance.csv
│   ├── market_performance.csv
│   ├── 03_region_performance.csv
│   ├── service_level_by_market.csv
│   ├── 05_scheduled_vs_actual.csv
│   ├── 06_delay_distribution.csv
│   ├── 07_category_performance.csv
│   └── 08_customer_segment_performance.csv
│
├── screenshots/
├── sql/
│   ├── 01_service_level_performance.sql
│   ├── 02_market_performance.sql
│   ├── 03_region_performance.sql
│   ├── 04_service_level_by_market.sql
│   ├── 05_scheduled_vs_actual.sql
│   ├── 06_delay_distribution.sql
│   ├── 07_category_performance.sql
│   └── 08_customer_segment_performance.sql
│
├── src/
│   ├── calculate_kpis.py
│   ├── prepare_data.py
│   ├── profile_data.py
│   ├── run_sql.py
│   └── validate_delivery_logic.py
│
├── Supply_Chain_Sales_Performance_Dashboard.pbix
├── requirements.txt
└── README.md