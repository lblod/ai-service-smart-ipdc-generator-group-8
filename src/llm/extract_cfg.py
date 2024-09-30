FORMAT_INSTRUCTIONS_KEY = 'format_instructions'
TEXT_KEY = 'text'
EXTRACTION_PROMPT = f'''You are an expert in extracting structured data from unstructured text.
Specifically, you have expert knowledge of so-called 'besluiten', which are decision made by a government (can be on different levels: municipality, province, etc.)
These documents are in Dutch, but since you are fluent in Dutch, this is no issue. You will extract data from the 'besluiten' in Dutch for a products and services catalog.

Besluit (unstructured text):
{{{TEXT_KEY}}}

{{{FORMAT_INSTRUCTIONS_KEY}}}'''