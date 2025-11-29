# audit_with_ai.py — Real Systemic Harm Ledger audit using any 2025 AI
# Just open this file → copy the prompt → paste into Grok/Claude/Perplexity/etc.

print("""
SYSTEMIC HARM LEDGER — FULL AUDIT WITH AI (2025)

1. Open any frontier model (no signup needed for basic use):
   • https://grok.x.ai
   • https://claude.ai
   • https://www.perplexity.ai
   • https://chatgpt.com
   • https://gemini.google.com

2. Paste this exact prompt (replace COMPANY):

────────────────────────────────────────────────────────────────────────────
You are a forensic auditor executing the Systemic Harm Ledger (November 2025).

Framework:
• https://github.com/coherenceanon/shl-bad-will-ledger/blob/main/ledger_of_will.md
• https://github.com/coherenceanon/shl-bad-will-ledger/blob/main/shl_model.md
• https://github.com/coherenceanon/shl-bad-will-ledger/blob/main/audit_of_will.md

Audit the company "COMPANY" using only public 2023–2025 data.

Answer every one of the 25 questions in audit_of_will.md with evidence and a 0 or 1.
Convert dimension totals (0–5 each) to 0–10 score using:
  0–1 checks → 0 pts | 2–3 checks → 1 pt | 4–5 checks → 2 pts per dimension

Final output (strict JSON only, no extra text):

{
  "company": "COMPANY",
  "score": 0,
  "quadrant": "Extraction|Performance|Drift|Stewardship",
  "shl_billions": 0.0,
  "verdict": "One brutal sentence"
}

SHL = (10 - score) × 3.9. Be ruthless. Do not accept corporate PR.
────────────────────────────────────────────────────────────────────────────

3. Press Enter.

You now have the real score, quadrant, and SHL in ~20 seconds.

MIT License · coherenceanon · November 2025
""")
