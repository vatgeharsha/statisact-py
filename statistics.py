def calculateStats(val):
    if len(val) == 0:
        return float("nan")
    return {"avg":sum(val)/len(val),"max":max(val),"min":min(val)}
