def risk_router(state):
    """
    Decide whether to call RAG + LLM
    """
    if state["risk"] == "Low":
        return "skip_advisory"
    else:
        return "do_advisory"