from langchain_ollama.llms import OllamaLLM
from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser
from typing import Type
from langchain_core.prompts import PromptTemplate
from src.llm.extract_cfg import EXTRACTION_PROMPT, FORMAT_INSTRUCTIONS_KEY, TEXT_KEY
from src.models import IPDCEntity

LLM = OllamaLLM(model='mistral-nemo', base_url='ollama.hackathon-ai-8.s.redhost.be')

def _create_pydantic_chain(pydantic_object: Type[BaseModel], prompt: str):
    output_parser = PydanticOutputParser(pydantic_object=pydantic_object)
    prompt_template = PromptTemplate.from_template(template=prompt, partial_variables={FORMAT_INSTRUCTIONS_KEY: output_parser.get_format_instructions()})
    return prompt_template | LLM | output_parser


def extract_ipdc_entity(text: str) -> IPDCEntity:
    extract_chain = _create_pydantic_chain(pydantic_object=IPDCEntity, prompt=EXTRACTION_PROMPT)
    return extract_chain.invoke({TEXT_KEY: text})
