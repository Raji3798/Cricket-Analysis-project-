# 🏏 Cricket Match Data Analytics Project

## 📌 Project Overview

This project focuses on **scraping, processing, analyzing, and visualizing cricket match data** from Cricsheet. It builds a complete data pipeline from raw JSON files to an interactive Power BI dashboard.

The system enables insights into:

* Player performance (batting & bowling)
* Team statistics
* Match outcomes
* Advanced analytics like all-rounders, fastest centuries, and last-over finishes

---

## 🎯 Objectives

* Automate data collection using web scraping
* Transform nested JSON data into structured format
* Store data in SQL database
* Perform analytical queries
* Create visual dashboards for insights

---

## 🛠️ Tech Stack

* Python (Pandas, JSON, SQLAlchemy)
* Selenium (Web Scraping)
* SQLite (Database)
* SQL (Data Analysis)
* Power BI (Visualization)
* Matplotlib, Seaborn, Plotly (EDA)

---

## 📂 Project Structure

```
cricsheet_project/
│
├── data/
│   ├── raw_json/
│   ├── processed/
│
├── scripts/
│   ├── scraper.py
│   ├── transform.py
│   ├── db_loader.py
│   ├── Cricket Analysis chart.pbix
│   ├── quires.ipynb
│
├── README.md
---

## ⚙️ Workflow

### 1. Data Scraping

* Downloaded cricket match JSON files from Cricsheet
* Used Python automation to extract datasets (ODI, T20, Test, IPL)

---

### 2. Data Transformation

* Parsed nested JSON files
* Flattened ball-by-ball data
* Extracted features:

  * batsman
  * bowler
  * runs
  * wickets
  * over

---

### 3. Database Creation

* Stored processed data into SQLite
* Created tables:

  * odi_matches
  * t20_matches
  * test_matches
  * ipl_matches

---

### 4. SQL Analysis

Performed advanced queries such as:

* Top batsmen across formats
* Top bowlers
* All-rounders
* Total centuries
* Fastest centuries
* Narrowest margin matches
* Last-over finishes

---

### 5. EDA (Exploratory Data Analysis)

* Created 10+ visualizations:

  * Top players
  * Runs distribution
  * Team performance
  * Over-wise analysis

---

### 6. Power BI Dashboard

Built an interactive dashboard with:

* KPI cards (Runs, Wickets, Matches)
* Top batsmen & bowlers
* Runs trend
* Filters (match type, team)

---

## 📊 Key Insights

* Identified top-performing batsmen across formats
* Analyzed bowling efficiency and economy
* Detected match pressure situations (last-over finishes)
* Found all-rounders with dual impact

---

## 🚀 How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run scripts

```
python scraper.py
python transform.py
python db_loader.py
```

### 3. Run Notebook

Open:

```
notebooks/eda.ipynb
```

### 4. Open Power BI Dashboard

Open:

```
powerbi/dashboard.pbix
```

---

## 📌 Future Improvements

* Add match winner & toss data
* Improve accuracy of fastest century calculation
* Deploy dashboard using Streamlit
* Add real-time cricket data APIs

---

## 🎯 Conclusion

This project demonstrates an **end-to-end data pipeline**, combining:

* Data engineering
* SQL analytics
* Visualization
* Business intelligence

---

## 👨‍💻 Author

Rajalakshmi
