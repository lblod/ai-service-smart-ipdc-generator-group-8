from src.llm.extract import extract_ipdc_data
from src.models import ProcessingRequest, ProcessingResponse


@app.get("/generate-ipdc")
def generated_ipdc(request: ProcessingRequest):
    ipdc_data = extract_ipdc_data(text=request.decision_text)
    return ProcessingResponse(entry=ipdc_data)
