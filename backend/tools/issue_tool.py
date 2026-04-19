def issue_tool(state):
    data = state["input"]
    issues = []

    if data["N"] < 50:
        issues.append({"type": "nitrogen", "severity": "high"})

    if data["Rainfall"] < 500:
        issues.append({"type": "rainfall", "severity": "medium"})

    if data["P"] < 40:
        issues.append({"type": "phosphorus", "severity": "high"})

    if data["Organic_Carbon"] < 0.5:
        issues.append({"type": "soil_fertility", "severity": "medium"})

    state["issues"] = issues
    return state