from pydantic import BaseModel, Field
from typing import List, Optional

RETURN_INSTRUCTION = 'The result should be returned in Dutch and can only be information or text from the main Besluit.'

IPDC_DESCRIPTION = f'''This property represents a free text Description of the Public Service.
The description is the text that potential users of the Public Service see in any public service catalogue.
Public administrations are encouraged to include a reasonable level of detail in the description, for instance including basic eligibility requirements for the particular Public Service and contact information.
{RETURN_INSTRUCTION}'''

IPDC_NAME = f'This property represents the official Name of the Public Service. {RETURN_INSTRUCTION}'

IPDC_COST = 'The Cost represents any costs related to the execution of a Public Service that the Agent consuming it needs to pay. The result should be returned in Dutch and can only be information or text from the main Besluit.'

IDPC_CONDITION = '''A normal requirement can specify the expected value that the requirement response has to contain, or a range of threshold values within which the requirement response has to fit in. 
The normal requirement may apply to a certain period of time. It also can provide a list of candidate evidences that the responder can use to prove the normal requirement.
The result should be returned in Dutch and can only be information or text from the main Besluit.'''

PROCEDURE_DESCRIPTION = f'A text field that outlines the procedure in detail in citizen readable language (do not refer to articles). {RETURN_INSTRUCTION}'

PROCEDURE_NAME = f'The name of the procedure. {RETURN_INSTRUCTION}'

class ProcessingRequest(BaseModel):
    decision_text: str


class IPDCBaseType(BaseModel):
    description: str
    name: Optional[str]


class IPDCProcedure(IPDCBaseType):
    '''Contains the specific rules, guidelines or procedures that need to be followed. It can include the terms of service, licence, and authentication requirements of the Public Service.'''
    description: str = Field(description=PROCEDURE_DESCRIPTION)
    name: Optional[str] = Field(description=PROCEDURE_NAME)


class IPDCCost(IPDCBaseType):
    description: str


class IPDCProof(IPDCBaseType):
    pass


class IPDCCondition(IPDCBaseType):
    proof: Optional[IPDCProof]
    description: str


# the LLM will see the descriptions of this class
class IPDCData(BaseModel):
    '''Data within an IPDC (products and services catalog) entry. All values within the fields are written in Dutch and contain information coming from the provided Besluit.'''
    description: str = Field(description=IPDC_DESCRIPTION)
    name: Optional[str] = Field(description=IPDC_NAME)
    procedure: Optional[IPDCProcedure]
    costs: Optional[List[IPDCCost]] = Field(description=IPDC_COST)
    conditions: List[IPDCCondition] = Field(description=IDPC_CONDITION)


# TODO: provide this class to the LLM instead
class IPDCDataFull(BaseModel):
    '''Data to include within an IPDC (products and services catalog) entry'''
    description: str = Field(description=IPDC_DESCRIPTION)
    name: str = Field(description=IPDC_NAME)
    procedures: List[IPDCProcedure] = []
    costs: List[str] = Field(description=IPDC_COST)
    conditions: List[IPDCCondition] = []


class ProcessingResponse(BaseModel):
    entry: IPDCData

