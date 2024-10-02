FORMAT_INSTRUCTIONS_KEY = 'format_instructions'
TEXT_KEY = 'text'
EXTRACTION_PROMPT = f'''You are an expert in extracting information from unstructured text into a JSON instance.
Specifically, you have expert knowledge of so-called decisions (in Dutch: 'besluit' or 'besluiten'), which are decisions made by a government (can be on different levels: municipality, province, etc.) on a Public Service.
You will extract the requested information from a provided decision under [> Decision (unstructured text):].
Since you are fluent in Dutch, you will extract the information in Dutch from a decision document written in Dutch.
This information will be made visible to citizens, agents and companies through the products and services catalog (IPDC).
Therefore, it is important to provide sufficient context such that those stakeholders can understand.
Do not invent or extrapolate any information; only use exact text from the provided decision.

> Decision (unstructured text):
>>>
{{{TEXT_KEY}}}
>>>

{{{FORMAT_INSTRUCTIONS_KEY}}}

Reminder that the values of all fields within the JSON instance need to be written in Dutch and need to contain only information coming from the decision provided above. Make sure your output is complete: all relevant information from the decision provided above must be extracted.'''
