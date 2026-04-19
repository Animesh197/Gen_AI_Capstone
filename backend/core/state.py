def create_initial_state(user_input: dict):
    return {
        "input": user_input,
        "processed_input": None,
        "prediction": None,
        "risk": None,
        "issues": [],
        "recommendations": [],
        "contributions": None,
        "context": None,
        "advisory": None
    }