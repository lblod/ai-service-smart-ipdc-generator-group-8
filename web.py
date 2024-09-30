from src.models import ProcessingRequest
from pydantic import BaseModel


class Result(BaseModel):
    description: str


@app.get("/generate-ipdc")
def generated_ipdc(request: ProcessingRequest):
    return Result(description='Maatregelen tijdens de crisisperiode voor handelaars: gratis aanvraag voor inname en plaatsing van verkeersborden door gemeentelijke diensten.')
