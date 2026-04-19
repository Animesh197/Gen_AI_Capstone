from backend.rag.retriever import retrieve_knowledge

def rag_tool(state):
    data = state["input"]
    issues = [i["type"] for i in state["issues"]]

    query = f"""
    Crop: {data['Crop_Type']}
    Issues: {issues}
    Soil: {data.get('Soil_Type')}
    Season: {data.get('Season')}
    """

    context = retrieve_knowledge(query)

    state["context"] = context
    return state