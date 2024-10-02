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

## LLM steps taken

### Mistral-Nemo & More complex data structure prompts
Our first attempt involved using Mistral Nemo with complex data structure prompts. This approach provided decent results but also presented several challenges.
   * Invalid JSON responses happened
   * Responses were sometimes mixed between Dutch and English
   * The content sometimes strayed from the intended purpose, with hallucinations and inconsistencies
   * Fully open-source model and relatively fast response time

### Transition to Llama 3.1 (70b)
We tested Llama 3.1 (70b), which yielded significantly better results but still had drawbacks.
   * The content was more aligned with the input text.
   * While accuracy improved overall, it wasn’t perfect but still a notable step forward
   * Response time increased immensely, up to 3 minutes per field
   * Utilizing examples in the prompts didn't help as Llama took info directly out of these examples even when context was adjusted
   * Non-European model with a slightly more restrictive license, however this would only be an issue with more than 700 million active users per month
     
### Simplified approach with single fields
We shifted to a more simplified prompting approach, using a single field that encapsulated each property. This provided some improvements.
   * Consistency improved across responses
   * Response time decreased due to having only one prompt which extracts all information at once

Utilizing both the stronger Llama model and the adjusted prompting approach allowed for better general performance for the extracted information. It's a shame
we couldn't use examples within the prompts but we needed to make a decision due to the high latency to prompt the model which reduced actual testing time.

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
