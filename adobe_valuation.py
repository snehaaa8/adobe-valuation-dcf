import yfinance as yf
import pandas as pd
from difflib import get_close_matches

def fuzzy_lookup(label, df):
    matches = get_close_matches(label, df.index, n=1, cutoff=0.5)
    if matches:
        return df.loc[matches[0]].iloc[0]
    else:
        print(f"[!] Row not found for '{label}' — closest matches: {get_close_matches(label, df.index, n=3)}")
        return None

def run_valuation():
    # Define the ticker
    ticker = yf.Ticker("ADBE")

    # Get company info and financials
    info = ticker.info
    balance = ticker.balance_sheet
    cashflow = ticker.cashflow
    financials = ticker.financials

    # Pull key data
    revenue = info.get("totalRevenue")
    ebit = financials.loc["EBIT"].iloc[0] if "EBIT" in financials.index else None
    net_income = financials.loc["Net Income"].iloc[0] if "Net Income" in financials.index else None

    # Fix for cash field name variation
    cash = None
    for label in ["Cash", "Cash And Cash Equivalents", "Cash And Short Term Investments"]:
        if label in balance.index:
            cash = balance.loc[label].iloc[0]
            break

    # Other inputs
    shares_outstanding = info.get("sharesOutstanding")
    current_price = info.get("currentPrice")
    beta = info.get("beta")
    debt = balance.loc["Long Term Debt"].iloc[0] if "Long Term Debt" in balance.index else 0

    # CAPM - Cost of Equity
    risk_free_rate = 0.045
    market_risk_premium = 0.055
    cost_of_equity = risk_free_rate + beta * market_risk_premium if beta else None

    # Estimate WACC
    equity_value = current_price * shares_outstanding if current_price and shares_outstanding else None
    firm_value = equity_value + debt if equity_value else None
    cost_of_debt = 0.035
    tax_rate = 0.15

    wacc = (
        (equity_value / firm_value) * cost_of_equity +
        (debt / firm_value) * cost_of_debt * (1 - tax_rate)
    ) if firm_value and cost_of_equity else None

    # FCF
    op_cash = fuzzy_lookup("Operating Cash Flow", cashflow)
    capex = fuzzy_lookup("Capital Expenditures", cashflow)
    fcf = op_cash - capex if op_cash is not None and capex is not None else None

    # Terminal Value & PV
    growth_rate = 0.05
    terminal_value = fcf * (1 + growth_rate) / (wacc - growth_rate) if fcf and wacc else None
    discount_factor = (1 + wacc) ** 5 if wacc else None
    present_value_tv = terminal_value / discount_factor if terminal_value and discount_factor else None

    # Equity value and intrinsic price
    intrinsic_equity_value = present_value_tv + cash - debt if present_value_tv and cash is not None else None
    intrinsic_value_per_share = intrinsic_equity_value / shares_outstanding if intrinsic_equity_value and shares_outstanding else None

    return {
        "current_price": current_price,
        "beta": beta,
        "cost_of_equity": cost_of_equity,
        "revenue": revenue,
        "ebit": ebit,
        "net_income": net_income,
        "debt": debt,
        "cash": cash,
        "shares_outstanding": shares_outstanding,
        "fcf": fcf,
        "wacc": wacc,
        "terminal_value": terminal_value,
        "present_value_tv": present_value_tv,
        "intrinsic_equity_value": intrinsic_equity_value,
        "intrinsic_value_per_share": intrinsic_value_per_share
    }

# --- Export to Excel only if run directly ---
if __name__ == "__main__":
    result = run_valuation()

    df_export = pd.DataFrame({
        "Metric": list(result.keys()),
        "Value": [f"${v:,.2f}" if isinstance(v, (int, float)) else v for v in result.values()]
    })

    df_export.to_excel("adobe_valuation_output.xlsx", index=False)
    print("\n✅ Valuation results exported to 'adobe_valuation_output.xlsx'")
