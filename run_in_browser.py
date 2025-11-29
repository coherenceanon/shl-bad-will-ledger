# run_in_browser.py — Systemic Harm Ledger (no install, no signup)
# Works instantly on online-python.com, programiz, onecompiler, etc.

from urllib.request import Request, urlopen
from urllib.parse import quote_plus
import re

def search(query):
    try:
        url = f"https://html.duckduckgo.com/html/?q={quote_plus(query)}"
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req, timeout=10).read().decode('utf-8')
        titles = re.findall(r'result__a">(.*?)</a>', page, re.DOTALL)[:8]
        return " ".join(titles).lower()
    except:
        return ""

def audit(company):
    pairs = [
        [f"{company} mission drift OR contradiction", f"{company} purpose alignment"],
        [f"{company} worker injuries OR burnout OR turnover", f"{company} employee support"],
        [f"{company} values vs actions OR hypocrisy", f"{company} incentives aligned"],
        [f"{company} leadership accountability OR blame", f"{company} owns failures"],
        [f"{company} regulatory fines OR lawsuits 2023..2025", f"{company} risk corrected"]
    ]
    scores = []
    for neg, pos in pairs:
        text = search(neg) + " " + search(pos)
        pos_count = sum(w in text for w in ["good","strong","fixed","aligned","safe","owns","corrected","excellent","support","care"])
        neg_count = sum(w in text for w in ["drift","injury","lawsuit","fine","blame","deflect","ignored","crisis","death","suicide","toxic"])
        scores.append(max(0, min(5, pos_count - neg_count + 5)))
    total = sum(scores)
    quadrant = "Stewardship" if total >= 20 else "Drift" if total >= 14 else "Performance" if total >= 9 else "Extraction"
    shl = round((25 - total) * 1.8, 1)
    print(f"{company} → {total}/25 | {quadrant} | ~${shl}B SHL")

# ←←←←←←←←←← CHANGE ONLY THIS LINE ←←←←←←←←←←
audit("Tesla")   # ← replace with any company you want
