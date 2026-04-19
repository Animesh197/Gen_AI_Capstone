from langchain_huggingface import HuggingFaceEndpoint
from backend.llm.prompt_template import build_prompt
from backend.rag.retriever import retrieve_knowledge
import os
from dotenv import load_dotenv

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-large",
    temperature=0.3,
    huggingfacehub_api_token=os.environ.get("HUGGINGFACEHUB_API_TOKEN", "")
)


def generate_advisory(user_input, prediction, risk, issues):
    query = f"{user_input['Crop_Type']} {' '.join(issues)}"

    context = retrieve_knowledge(query)

    prompt = build_prompt(user_input, prediction, risk, issues, context)

    try:
        response = llm(prompt)
    except Exception as e:
        print("LLM ERROR:", str(e))
        raise e

    return response, context