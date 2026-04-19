def recommend_tool(state):
    mapping = {
        "nitrogen_deficiency":   ("Apply urea fertilizer to boost nitrogen levels", "high"),
        "phosphorus_deficiency": ("Apply DAP fertilizer to improve phosphorus content", "high"),
        "potassium_deficiency":  ("Use potash fertilizers to restore potassium levels", "medium"),
        "low_rainfall":          ("Install drip or sprinkler irrigation system", "medium"),
        "low_soil_fertility":    ("Add compost or organic manure to improve soil fertility", "medium"),
        "acidic_soil":           ("Apply lime to raise soil pH to optimal range", "medium"),
        "alkaline_soil":         ("Use gypsum or sulfur to lower soil pH", "medium"),
        "heat_stress":           ("Switch to heat-resistant crop varieties and increase irrigation", "high"),
    }

    recs = []
    for issue in state["issues"]:
        entry = mapping.get(issue["type"])
        if entry:
            recs.append({
                "action": entry[0],
                "priority": issue["severity"]
            })

    state["recommendations"] = recs
    return state
