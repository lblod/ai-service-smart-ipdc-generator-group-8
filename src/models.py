from pydantic import BaseModel


class ProcessingRequest(BaseModel):
    decision_text: str


class IPDCEntity(BaseModel):
    description: str
