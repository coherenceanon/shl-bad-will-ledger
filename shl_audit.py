# audit.py — Official Systemic Harm Ledger scoring (November 2025)
# Run: python audit.py

print("""
SYSTEMIC HARM LEDGER — OFFICIAL SCORING (Nov 2025)

Count the checks for each dimension (0–5):

Direction      : __ / 5
Burden         : __ / 5
Coherence      : __ / 5
Accountability : __ / 5
Risk           : __ / 5

Scoring per dimension:
  0–1 checks → 0 points
  2–3 checks → 1 point
  4–5 checks → 2 points

Enter the five dimension point values (0, 1, or 2 each), space-separated:
Example: 0 1 2 1 2
""")

raw = input("→ ").strip()
nums = [int(x) for x in raw.split()[:5] if x in "012"]

if len(nums) != 5:
    print("Error: exactly five numbers required (0, 1, or 2)")
    exit()

total = sum(nums)

if total >= 9:
    quad = "Stewardship"
    shl = round((10 - total) * 3.9, 1)
elif total >= 6:
    quad = "Drift"
    shl = round((10 - total) * 3.9, 1)
elif total >= 3:
    quad = "Performance"
    shl = round((10 - total) * 3.9, 1)
else:
    quad = "Extraction"
    shl = round((10 - total) * 3.9, 1)

print(f"\nTOTAL SCORE : {total}/10 → {quad}")
print(f"SHL estimate : ~${shl}B")
print("\nNo AI. No scraping. No excuses.")
