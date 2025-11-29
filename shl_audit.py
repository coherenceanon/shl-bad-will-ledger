# audit.py — Official Systemic Harm Ledger scoring (2025)
# Run: python audit.py   → fills in the real 0–10 score

print("""
SYSTEMIC HARM LEDGER — OFFICIAL SCORING (Nov 2025)

You have just completed the 25-question Audit of Will.
Now count the checks in each dimension:

Direction      : __ / 5
Burden         : __ / 5  
Coherence      : __ / 5
Accountability : __ / 5
Risk           : __ / 5

Scoring per dimension:
  0–1 checks → 0 points
  2–3 checks → 1 point
  4–5 checks → 2 points

Enter the five numbers below (example: 0 1 2 1 2)
""")

raw = input("→ ").strip()
nums = [int(x) for x in raw.split()[:5]]

total = sum(
    0 if n <= 1 else
    1 if n <= 3 else
    2 for n in nums
)

quad = (
    "Extraction"  if total <= 2 else
    "Performance" if total <= 5 else
    "Drift"       if total <= 8 else
    "Stewardship"
)

shl = round((10 - total) * 3.9, 1)   # 10→$0B, 0→$39B (calibrated Nov 2025)

print(f"\nTOTAL SCORE : {total}/10 → {quad}")
print(f"SHL estimate: ~${shl}B")
print("\nThis is the real, final, canonical number.")
print("No AI. No scraping. No excuses.")
