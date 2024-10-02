# ai-service-smart-ipdc-generator-group-8
This is the implementation of the AI service for the smart IPDC generator application created during the hackaton.

## General overview
The purpose of this service is to automatically translate incoming text from a decision (Besluit) into a structured format through a set of different AI techniques.
The output for a request will be a structured model, containing specific properties that align with the IPDC data model object ['Instantie'](https://productencatalogus.data.vlaanderen.be/doc/implementatiemodel/ipdc-lpdc/#Instantie).

## Process
The process of AI extraction / translation is as follows:
1. Extraction of information with an LLM
    * A detailed prompt to instruct the LLM is populated with the incoming decision text. This prompt is then provided to the LLM.
    * The response from the LLM is validated by a Pydantic model in order to ensure a structured output object that can be used in subequent parts of the process.
    Output: An object containing a **name** and a **description** for the public service, a description of the **procedures**, a description of the **costs** and a description of the **conditions**.
2. Classification based on the information extracted by the LLM through a set of classification services (each service implements a classification model for a specific entity)
    * Asynchronously request classifications from the **theme**, **type** and **doelgroep** classifier services
3. Translate into final output
    * All received objects are used to populate the final output that aligns with the IPDC data model object

## Usage

### generate-ipdc endpoint
The endpoint `/generate-ipdc` expects a POST request with the following structure:
```json
{
    "decision_text": "flat text extracted from the decision document(s)"
}
```
It will return a JSON response with the following structure:
```python
class IPDCEntry(BaseModel):
    description: str
    name: str
    procedure: List[IPDCProcedure] = []
    cost: List[IPDCCost] = []
    condition: List[IPDCCondition] = []
    theme: List[str]
    type: List[str]
    doelgroep: List[str]
```
where IPDCProcedure, IPDCCost and IPDCCondition correspond to the format defined by ['Instantie'](https://productencatalogus.data.vlaanderen.be/doc/implementatiemodel/ipdc-lpdc/#Instantie).
