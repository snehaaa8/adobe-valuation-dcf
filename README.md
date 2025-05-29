# 💼 Adobe Inc. Valuation using Python, Plotly & DCF Analysis

This project estimates the **intrinsic value of Adobe Inc. (ADBE)** using:

* ✅ Discounted Cash Flow (DCF) modeling
* 📉 Comparable Company Analysis (P/E, P/B, ROE, etc.)
* 📈 Historical financial trends and risk metrics
* 🐍 Python automation (yfinance, NumPy, Plotly)

> Final deliverables include a Jupyter notebook, Excel valuation models, interactive charts (HTML), and Python scripts.

---

## 📂 Project Structure

```
adobe-valuation/
├── adobe_valuation_notebook.ipynb      # Main notebook with visualizations
├── adobe_valuation.py                  # Python module to compute valuation
├── adobe_valuation_output.xlsx         # Python-exported valuation data
├── Adobe_Valuation_Summary.docx        # Optional summary report
├── dcf_waterfall.html                  # HTML chart: DCF breakdown
├── historical_financials.html          # HTML chart: Revenue, Net Income, FCF
├── peer_comparables.html               # HTML chart: P/E, P/B, ROE
├── risk_growth_analysis.html           # HTML chart: volatility, growth
└── valuation_summary.html              # HTML chart: Intrinsic vs Market Price
```

---

## 📊 Key Components

### 📈 Intrinsic Valuation via DCF

* Forecasted Free Cash Flows (5 yrs)
* Terminal Value based on growth assumptions
* WACC computed from inputs
* Present Value of Equity and Value/Share

### 🔍 Market Multiples Comparison

* P/E, P/B, ROE, Profit Margin for ADBE vs. peers (MSFT, ORCL, CRM)

### 📉 Risk & Growth Analysis

* Volatility (30-day rolling)
* Revenue growth trend

---

## ❓ Questions Answered

* 📌 What is Adobe’s intrinsic value per share based on DCF?
  → \~\$150.68, compared to a market price of \~\$412
* 📌 Is Adobe overvalued or undervalued?
  → The company appears **overvalued** by \~63%
* 📌 How do Adobe’s valuation metrics compare to peers?
  → Adobe lags behind some peers on ROE but maintains high profit margins
* 📌 What are the recent financial performance trends?
  → Steady revenue and FCF growth from 2021–2025
* 📌 How volatile is Adobe’s stock?
  → Moderate volatility over a 5-year period based on rolling standard deviation

---

## 🛠️ Languages & Tools Used

| Language / Tool    | Purpose                               |
| ------------------ | ------------------------------------- |
| `Python 3.11`      | Main scripting & automation           |
| `Jupyter Notebook` | Interactive analysis                  |
| `Pandas` / `NumPy` | Financial data handling & computation |
| `Plotly`           | Interactive visualizations            |
| `yfinance`         | Live financial data pull              |
| `Excel`            | Manual model for cross-validation     |

> 📘 The manual financial data (used in the Excel file and Word summary) was sourced directly from Adobe's latest **10-K and 10-Q** filings.

---

## 💡 How to Run

1. Clone repo / download files
2. Open `adobe_valuation_notebook.ipynb` in Jupyter or VS Code
3. Run cells to generate updated charts
4. Optional: open `.html` files in browser

---

## 📦 Requirements

Install dependencies:

```bash
pip install yfinance numpy pandas plotly
```

---

## 📌 Author & Credit

Built by **Sneha Dutt** using live financials and Python automation.
This project showcases data-driven financial valuation for Adobe Inc.
