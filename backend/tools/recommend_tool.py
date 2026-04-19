def recommend_tool(state):
    mapping = {
        "nitrogen_deficiency":   ("Apply urea fertilizer (46-0-0) at 100-150 kg/ha to boost nitrogen levels", "high"),
        "phosphorus_deficiency": ("Apply DAP fertilizer (18-46-0) at 100 kg/ha to improve phosphorus content", "high"),
        "potassium_deficiency":  ("Use muriate of potash (0-0-60) at 60-80 kg/ha to restore potassium levels", "medium"),
        "low_rainfall":          ("Install drip or sprinkler irrigation system for water management", "high"),
        "low_soil_moisture":     ("Increase irrigation frequency and consider mulching to retain soil moisture", "medium"),
        "low_soil_fertility":    ("Add farmyard manure (10-15 t/ha) or compost (5-8 t/ha) to improve soil fertility", "medium"),
        "acidic_soil":           ("Apply agricultural lime (2-4 t/ha) to raise soil pH to optimal range", "medium"),
        "alkaline_soil":         ("Use gypsum (2-3 t/ha) or elemental sulfur (200-500 kg/ha) to lower soil pH", "medium"),
        "heat_stress":           ("Use heat-tolerant varieties and increase irrigation frequency during hot periods", "high"),
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
