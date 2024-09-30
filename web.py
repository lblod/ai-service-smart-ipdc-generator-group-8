from src.models import ProcessingRequest, IPDCEntry
from pydantic import BaseModel
from src.llm.extract import extract_ipdc_data

class Result(BaseModel):
    description: str


@app.get("/mock-ipdc")
def mock_ipdc():
    return Result(description='Maatregelen tijdens de crisisperiode voor handelaars: gratis aanvraag voor inname en plaatsing van verkeersborden door gemeentelijke diensten.')


@app.post("/generate-ipdc")
def generated_ipdc(request: ProcessingRequest) -> IPDCEntry:
    return extract_ipdc_data(text=request.decision_text)
