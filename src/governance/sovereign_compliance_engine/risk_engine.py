def calculate_risk(context: dict) -> int:
    score = 0
    score += 40 if context.get("amount", 0) > 10000 else 0
    score += 30 if not context.get("kyc", False) else 0
    score += 20 if context.get("cross_border", False) else 0
    return min(score, 100)
