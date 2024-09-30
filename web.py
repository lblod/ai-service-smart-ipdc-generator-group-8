from src.llm.extract import extract_ipdc_entity
from src.models import ProcessingRequest


@app.get("/generate-ipdc")
def generated_ipdc(request: ProcessingRequest):
    idpc_entity = extract_ipdc_entity(text=request.decision_text)
    return idpc_entity.model_dump()
