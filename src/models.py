from pydantic import BaseModel, Field
from typing import List, Optional

RETURN_INSTRUCTION = 'This text is written in Dutch and contains only information coming from the provided Besluit.'

IPDC_DESCRIPTION = f'''This property represents a free text Description of the Public Service.
The description is the text that potential users of the Public Service see in any public service catalogue.
Public administrations are encouraged to include a reasonable level of detail in the description, for instance including basic eligibility requirements for the particular Public Service and contact information.
{RETURN_INSTRUCTION}'''

IPDC_NAME = f'''This property represents the official Name of the Public Service.
{RETURN_INSTRUCTION}'''

IPDC_COST = f'The Cost represents any costs related to the execution of a Public Service that the Agent consuming it needs to pay. {RETURN_INSTRUCTION}'
IPDC_COST_NAME = f'This property represents the official Name of the Cost. {RETURN_INSTRUCTION}'

IDPC_CONDITION = f'''A normal requirement can specify the expected value that the requirement response has to contain, or a range of threshold values within which the requirement response has to fit in. 
The normal requirement may apply to a certain period of time. It also can provide a list of candidate evidences that the responder can use to prove the normal requirement.
{RETURN_INSTRUCTION}'''
IPDC_CONDITION_NAME = f'''This property represents the official Name of the Condition. {RETURN_INSTRUCTION}'''

PROCEDURE_DESCRIPTION = f'''Outlines the procedure in detail in citizen readable language (do not refer to articles). {RETURN_INSTRUCTION}'''

PROCEDURE_NAME = f'''The name of the procedure. {RETURN_INSTRUCTION}'''


# the LLM will see the descriptions of these classes
class IPDCBaseType(BaseModel):
    description: str
    name: Optional[str]


class IPDCProcedure(BaseModel):
    '''Contains the specific rules, guidelines or procedures that need to be followed by the citizen. It can include the terms of service, licence, and authentication requirements of the Public Service.'''
    description: str = Field(description=PROCEDURE_DESCRIPTION)
    name: Optional[str] = Field(description=PROCEDURE_NAME)


class IPDCCostData(IPDCBaseType):
    costs: Optional[List[str]] = Field(description=IPDC_COST)
    name: Optional[str]


class IPDCProof(IPDCBaseType):
    pass


class IPDCConditionData(IPDCBaseType):
    proof: Optional[IPDCProof]
    conditions: List[str] = Field(description=IDPC_CONDITION)


class IPDCData(BaseModel):
    '''Data to include within an IPDC (products and services catalog) entry'''
    description: str = Field(description=IPDC_DESCRIPTION)
    name: str = Field(description=IPDC_NAME)


# models for the API
class ProcessingRequest(BaseModel):
    decision_text: str


class IPDCCost(IPDCBaseType):
    pass


class IPDCCondition(IPDCBaseType):
    proof: Optional[IPDCProof]


class IPDCEntry(BaseModel):
    description: str
    name: str
    procedure: List[IPDCProcedure] = []
    cost: List[IPDCCost] = []
    condition: List[IPDCCondition] = []
    theme: List[str]
    type: List[str]
    doelgroep: List[str]


class ProcessingResponse(BaseModel):
    ipdc_entry: IPDCEntry
