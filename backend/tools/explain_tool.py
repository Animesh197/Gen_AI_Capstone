from backend.intelligence.explainer import get_feature_contributions


def explain_tool(state, model, scaler):
    contrib = get_feature_contributions(
        model,
        state["processed_input"],
        scaler,
        state["processed_input"].columns
    )

    state["contributions"] = contrib
    
    # Extract top negative contributors for issue detection enhancement
    negative_contribs = contrib[contrib["Contribution"] < 0].head(5)
    state["ml_negative_factors"] = negative_contribs["Feature"].tolist() if len(negative_contribs) > 0 else []
    
    return state