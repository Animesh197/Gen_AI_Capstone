from backend.tools.preprocess_tool import preprocess_tool
from backend.tools.predict_tool import predict_tool
from backend.tools.issue_tool import issue_tool
from backend.tools.risk_tool import risk_tool
from backend.tools.recommend_tool import recommend_tool
from backend.tools.explain_tool import explain_tool
from backend.tools.rag_tool import rag_tool
from backend.tools.advisory_tool import advisory_tool


def get_nodes(model, scaler, columns):
    """
    Returns all node functions with dependencies injected.
    """

    def preprocess_node(state):
        return preprocess_tool(state, columns)

    def predict_node(state):
        return predict_tool(state, model, scaler)

    def issue_node(state):
        return issue_tool(state)

    def risk_node(state):
        return risk_tool(state)

    def recommend_node(state):
        return recommend_tool(state)

    def explain_node(state):
        return explain_tool(state, model, scaler)

    def rag_node(state):
        return rag_tool(state)

    def advisory_node(state):
        return advisory_tool(state)

    return {
        "preprocess": preprocess_node,
        "predict": predict_node,
        "issue": issue_node,
        "risk": risk_node,
        "recommend": recommend_node,
        "explain": explain_node,
        "rag": rag_node,
        "advisory": advisory_node
    }