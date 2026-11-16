"""Explainable account ranking; no external dependencies."""
from datetime import date

WEIGHTS = {"industry": 30, "size": 20, "region": 15, "signals": 25, "evidence": 10}

def score_account(account, icp):
    """Return a 0-100 score and transparent component explanations."""
    signals = account.get("signals", [])
    evidence = [s for s in signals if s.get("source_url") and s.get("observed_at")]
    components = {
        "industry": WEIGHTS["industry"] if account.get("industry") in icp.get("industries", []) else 0,
        "size": WEIGHTS["size"] if icp.get("min_employees", 0) <= account.get("employees", -1) <= icp.get("max_employees", 10**9) else 0,
        "region": WEIGHTS["region"] if account.get("region") in icp.get("regions", []) else 0,
        "signals": min(WEIGHTS["signals"], sum(max(0, min(10, int(s.get("strength", 0)))) for s in signals)),
        "evidence": min(WEIGHTS["evidence"], len(evidence) * 5),
    }
    return {"score": sum(components.values()), "components": components, "evidence_count": len(evidence), "signal_count": len(signals)}

def rank_accounts(accounts, icp):
    return sorted([{**a, "assessment": score_account(a, icp)} for a in accounts], key=lambda a: (-a["assessment"]["score"], a["name"]))
