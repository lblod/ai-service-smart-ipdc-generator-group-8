from pydantic import BaseModel, Field
from typing import List, Optional

IPDC_DESCRIPTION = '''This property represents a free text Description of the Public Service.
The description is the text that potential users of the Public Service see in any public service catalogue.
Public administrations are encouraged to include a reasonable level of detail in the description, for instance including basic eligibility requirements for the particular Public Service and contact information.'''

IPDC_NAME = 'This property represents the official Name of the Public Service.'


class ProcessingRequest(BaseModel):
    decision_text: str


class IPDCBaseType(BaseModel):
    description: str
    name: Optional[str]


class IPDCProcedure(IPDCBaseType):
    pass


class IPDCCost(IPDCBaseType):
    pass


class IPDCProof(IPDCBaseType):
    pass


class IPDCCondition(IPDCBaseType):
    proof: Optional[IPDCProof]


# the LLM will see the descriptions of this class
class IPDCData(BaseModel):
    '''Data to include within an IPDC (products and services catalog) entry'''
    description: str = Field(description=IPDC_DESCRIPTION)
    name: str = Field(description=IPDC_NAME)


# TODO: provide this class to the LLM instead
class IPDCDataFull(BaseModel):
    '''Data to include within an IPDC (products and services catalog) entry'''
    description: str = Field(description=IPDC_DESCRIPTION)
    name: str = Field(description=IPDC_NAME)
    procedures: List[IPDCProcedure] = []
    costs: List[IPDCCost] = []
    conditions: List[IPDCCondition] = []


class ProcessingResponse(BaseModel):
    entry: IPDCData
