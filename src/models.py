from pydantic import BaseModel, Field
from typing import List, Optional

IPDC_DESCRIPTION = '''This property represents a free text Description of the Public Service.
The description is the text that potential users of the Public Service see in any public service catalogue.
Public administrations are encouraged to include a reasonable level of detail in the description, for instance including basic eligibility requirements for the particular Public Service and contact information.'''

IPDC_NAME = 'This property represents the official Name of the Public Service.'

IPDC_COST = 'The Cost represents any costs related to the execution of a Public Service that the Agent consuming it needs to pay. '

IPDC_COST_NAME = 'This property represents the official Name of the Cost. '

IDPC_CONDITION = '''A normal condition can specify the expected value that the condition response has to contain, or a range of threshold values within which the condition response has to fit in. 
The normal condition may apply to a certain period of time. It also can provide a list of candidate evidences that the responder can use to prove the normal condition.'''

IPDC_CONDITION_NAME = '''This property represents the official Name of the Condition. '''

class ProcessingRequest(BaseModel):
    decision_text: str


class IPDCBaseType(BaseModel):
    description: str
    name: Optional[str]


class IPDCProcedure(IPDCBaseType):
    pass


class IPDCCost(IPDCBaseType):
    costs: Optional[List[str]] = Field(description=IPDC_COST)
    name: Optional[str]


class IPDCProof(IPDCBaseType):
    pass


class IPDCCondition(IPDCBaseType):
    proof: Optional[IPDCProof]
    conditions: List[str] = Field(description=IDPC_CONDITION)


# the LLM will see the descriptions of this class
class IPDCData(BaseModel):
    '''Data to include within an IPDC (products and services catalog) entry'''
    # description: str = Field(description=IPDC_DESCRIPTION)
    # name: Optional[str] = Field(description=IPDC_NAME)
    costs: IPDCCost
    conditions: IPDCCondition


# TODO: provide this class to the LLM instead
class IPDCDataFull(BaseModel):
    '''Data to include within an IPDC (products and services catalog) entry'''
    description: str = Field(description=IPDC_DESCRIPTION)
    name: Optional[str] = Field(description=IPDC_NAME)
    procedures: List[IPDCProcedure] = []
    costs: Optional[List[IPDCCost]] = Field(description=IPDC_COST, name=IPDC_COST_NAME)
    conditions: List[IPDCCondition] = Field(description=IDPC_CONDITION)


class ProcessingResponse(BaseModel):
    entry: IPDCData

