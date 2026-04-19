def recommend_tool(state):
    mapping = {
        "nitrogen": "Apply urea fertilizer",
        "rainfall": "Use irrigation system"
    }

    recs = []

    for issue in state["issues"]:
        action = mapping.get(issue["type"])
        if action:
            recs.append({
                "action": action,
                "priority": issue["severity"]
            })

    state["recommendations"] = recs
    return state