from backend.intelligence.explainer import get_feature_contributions

def explain_tool(state, model, scaler):
    contrib = get_feature_contributions(
        model,
        state["processed_input"],
        scaler,
        state["processed_input"].columns
    )

    state["contributions"] = contrib
    return state