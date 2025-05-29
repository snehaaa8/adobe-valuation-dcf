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
├── adobe_analysis.ipynb               # Main notebook with visualizations
├── adobe_valuation.py                 # Python module to compute valuation
├── adobe_valuation_output.xlsx        # Python-exported valuation data
├── Adobe_DCF_Prefilled.xlsx           # Manual Excel-based DCF model
├── Adobe_Valuation_Summary.docx       # Optional summary report
├── dcf_waterfall.html                 # HTML chart: DCF breakdown
├── historical_financials.html         # HTML chart: Revenue, Net Income, FCF
├── peer_comparables.html              # HTML chart: P/E, P/B, ROE
├── risk_growth_analysis.html          # HTML chart: volatility, growth
└── valuation_summary.html             # HTML chart: Intrinsic vs Market Price
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

## 💡 How to Run

1. Clone repo / download files
2. Open `adobe_analysis.ipynb` in Jupyter or VS Code
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

Built by Sneha Dutt using live financials and Python automation. Project showcases data-driven financial valuation for Adobe Inc.

---

## 📤 Optional Extensions

* [ ] Add Power BI or Tableau dashboard
* [ ] Publish findings on LinkedIn or GitHub Pages
* [ ] Integrate Alpha Vantage or SEC API for enhanced data

---

> 📁 This is a resume-ready project that combines technical and financial modeling skills. Perfect for analyst interviews, portfolio showcases, or investment case studies.
