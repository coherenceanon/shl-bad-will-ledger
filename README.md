# Systemic Harm Ledger
Turns Bad Will into a balance-sheet liability using only public data.

## Core Files
- **[Ledger of Will](ledger_of_will.md)** – philosophical 2×2 framework (Faith × Will)
- **[SHL Model](shl_model.md)** – full mathematical model and SHL formula
- **[Audit of Will](audit_of_will.md)** – the 25-question audit template

## Repository files
- `README.md` – this file
- `ledger_of_will.md`
- `shl_model.md`
- `audit_of_will.md`
- `shl_audit.py` – tiny manual scorer (Method 1)
- `shl_audit_with_ai.py` – optional script for any AI assistant (Method 2)

## Run an Audit (choose one method)

### Method 1 – Manual (recommended, fully auditable)
1. Answer all 25 questions in `audit_of_will.md` with public evidence → 0 or 1  
2. Count 1s per dimension (0–5 each)  
3. Score each dimension: 0–1 ones → 0 pts | 2–3 ones → 1 pt | 4–5 ones → 2 pts  
4. Total score = sum of five dimension points (max 10)  
5. **SHL (billions USD) = (10 − total_score) × 3.9**

### Method 2 – AI-Assisted (any frontier model)
Paste this **exact prompt** into Grok, Claude, Gemini, ChatGPT, Llama 3.1, or any capable model:

"You are a forensic auditor executing the Systemic Harm Ledger (November 2025).
Audit the company "[COMPANY]" using only public 2023–2025 data.
Answer every one of the 25 questions in audit_of_will.md with evidence and a 0 or 1.
Use the official scoring rules and return strict JSON only."

