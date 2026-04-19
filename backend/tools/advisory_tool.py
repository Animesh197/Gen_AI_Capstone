from backend.llm.advisor import generate_advisory

def advisory_tool(state):
    try:
        advisory, context = generate_advisory(
            state["input"],
            state["prediction"],
            state["risk"],
            state["issues"]
        )
    except:
        advisory = {
            "summary": "Failed",
            "recommendations": []
        }

    state["advisory"] = advisory
    return state