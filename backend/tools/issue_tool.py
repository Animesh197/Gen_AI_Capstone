def issue_tool(state):
    data = state["input"]
    issues = []

    # Nitrogen
    if data["N"] < 50:
        issues.append({"type": "nitrogen_deficiency", "severity": "high"})

    # Phosphorus
    if data["P"] < 40:
        issues.append({"type": "phosphorus_deficiency", "severity": "high"})

    # Potassium
    if data["K"] < 40:
        issues.append({"type": "potassium_deficiency", "severity": "medium"})

    # Rainfall
    if data["Rainfall"] < 500:
        issues.append({"type": "low_rainfall", "severity": "medium"})

    # Organic Carbon
    if data["Organic_Carbon"] < 0.5:
        issues.append({"type": "low_soil_fertility", "severity": "medium"})

    # Soil pH
    if data["Soil_pH"] < 5.5:
        issues.append({"type": "acidic_soil", "severity": "medium"})
    elif data["Soil_pH"] > 7.5:
        issues.append({"type": "alkaline_soil", "severity": "medium"})

    # Temperature
    if data["Temperature"] > 38:
        issues.append({"type": "heat_stress", "severity": "high"})

    state["issues"] = issues
    return state
