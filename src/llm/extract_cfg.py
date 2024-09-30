FORMAT_INSTRUCTIONS_KEY = 'format_instructions'
TEXT_KEY = 'text'
EXTRACTION_PROMPT = f'''You are an expert in extracting information from unstructured text into a JSON instance.
Specifically, you have expert knowledge of so-called 'besluiten', which are decisions made by a government (can be on different levels: municipality, province, etc.) on a Public Service.
A Besluit document is written in Dutch, but since you are fluent in Dutch, this is no issue. You will convert the provided Besluit (decision) to structured data for the products and services catalog (IPDC) that is visible to citizens.
Do not invent or extrapolate any information; only use exact text from the provided Besluit.
Provide sufficient context such that an average citizen can understand.

Besluit (unstructured text):
{{{TEXT_KEY}}}

{{{FORMAT_INSTRUCTIONS_KEY}}}'''