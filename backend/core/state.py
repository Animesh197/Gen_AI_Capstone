from typing import TypedDict, Optional, Any


class FarmState(TypedDict):
    input: dict
    processed_input: Optional[Any]
    prediction: Optional[float]
    risk: Optional[str]
    issues: list
    recommendations: list
    contributions: Optional[Any]
    ml_negative_factors: list  # New field for ML-detected negative factors
    context: Optional[str]
    advisory: Optional[dict]


def create_initial_state(user_input: dict) -> FarmState:
    return {
        "input": user_input,
        "processed_input": None,
        "prediction": None,
        "risk": None,
        "issues": [],
        "recommendations": [],
        "contributions": None,
        "ml_negative_factors": [],  # Initialize empty
        "context": None,
        "advisory": None
    }
