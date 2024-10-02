from pydantic import BaseModel, Field

TITLE = 'The official Name of the Public Service. It is used as a title in the web application.'
DESCRIPTION = '''A text description of the Public Service that potential users of the Public Service can see in any public service catalogue.
You are encouraged to include a reasonable level of detail in the description, for instance including basic eligibility requirements for the particular Public Service and contact information.'''
PROCEDURES = '''A detailed outline of each of the procedures in citizen readable language (do not refer to articles). Contains the specific rules, guidelines or procedures that need to be followed.
It can include the terms of service, licence, and authentication requirements of the Public Service. If multiple procedures are applicable for the Public Service, make sure to include all of them.'''
COSTS = '''A detailed outline of the costs related to the execution or utilization of the Public Service that the user of that Public Service needs to pay. If multiple costs are applicable for the Public Service, make sure to include all of them.'''
CONDITIONS = '''A detailed outline of the requirements of the Public Service. A requirement can specify the expected value that the requirement response has to contain, or a range of threshold values which the requirement response has to fit within. 
A requirement may apply to a certain period of time. It can also provide a list of candidate evidences that the responder can use to prove the requirement. If multiple requirements are applicable for the Public Service, make sure to include all of them.'''

# simplified approach
class IPDCInformationToExtract(BaseModel):
    '''Information to extract from the provided decision for a publicly available products and services catalog. All field values are written in Dutch and contain only information coming from the provided decision.'''
    title: str = Field(description=TITLE)
    description: str = Field(description=DESCRIPTION)
    procedures: str = Field(description=PROCEDURES)
    costs: str = Field(description=COSTS)
    conditions: str = Field(description=CONDITIONS)
