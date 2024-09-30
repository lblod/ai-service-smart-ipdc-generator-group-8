FORMAT_INSTRUCTIONS_KEY = 'format_instructions'
TEXT_KEY = 'text'
EXTRACTION_PROMPT = f'''You are an expert in extracting structured data from unstructured text.
Extract the entity from the following text:
{{{TEXT_KEY}}}

{{{FORMAT_INSTRUCTIONS_KEY}}}'''