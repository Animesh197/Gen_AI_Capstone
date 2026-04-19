from backend.core.state import create_initial_state
from backend.graph.graph_builder import build_graph

import joblib

# ================= LOAD ARTIFACTS (LOAD ONCE) =================
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("column.pkl")


# ================= BUILD GRAPH (PASS DEPENDENCIES) =================
app_graph = build_graph(
    model=model,
    scaler=scaler,
    columns=columns
)


def run_pipeline(user_input: dict):
    """
    Main entry point for the system.
    Executes LangGraph with initial state.
    """

    # Step 1: Initialize state
    state = create_initial_state(user_input)

    # Step 2: Run graph
    final_state = app_graph.invoke(state)

    return final_state