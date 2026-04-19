from backend.preprocessor import preprocess_input

def preprocess_tool(state, columns):
    processed = preprocess_input(state["input"], columns)
    state["processed_input"] = processed
    return state