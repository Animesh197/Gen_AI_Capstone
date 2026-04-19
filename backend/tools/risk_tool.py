def risk_tool(state):
    crop = state["input"]["Crop_Type"]
    pred = state["prediction"]

    baseline = {
        "Wheat": 3.5,
        "Rice": 4.0,
        "Maize": 3.0
    }

    base = baseline.get(crop, 3.0)
    ratio = pred / base

    if ratio < 0.6:
        risk = "High"
    elif ratio < 0.85:
        risk = "Moderate"
    else:
        risk = "Low"

    state["risk"] = risk
    return state