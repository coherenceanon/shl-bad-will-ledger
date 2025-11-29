# Systemic Harm Ledger  
Measuring Bad Will as a Balance-Sheet Liability

This repository contains the complete open-source implementation of three interconnected frameworks:

- **The Ledger of Will** → 2×2 diagnostic (Good/Bad Faith × Good/Bad Will)  
- **Systemic Harm Liability (SHL) Model** → turns Bad Will into a quantifiable contingent liability with two permanent valuation dings  
- **The Audit of Will** → 25-point public-data checklist (0–25 score) that places any organisation on the ledger

No regulators required.  
No internal access needed.  
Anyone can run it today.

## Files
- `ledger_of_will.md` — full original text  
- `shl_model.md` — full SHL mathematics and examples  
- `audit_of_will.md` — full 25-question audit  
- `scoring_engine.py` — one-click Python script (run on any company)  
- `SCORES.md` — 30 live scores as of 29 Nov 2025  
- `LICENSE` — MIT (fork and improve freely)

## 10-Second Demo
```bash
pip install -r requirements.txt
python scoring_engine.py "Tesla"
# → Tesla → 1/25 | Extraction | ~$43B SHL
