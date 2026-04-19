from backend.predictor import predict_yield

def predict_tool(state, model, scaler):
    pred = predict_yield(model, scaler, state["processed_input"])
    state["prediction"] = float(pred)
    return state