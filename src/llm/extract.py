from langchain_ollama.llms import OllamaLLM
from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser
from typing import Type
from langchain_core.prompts import PromptTemplate
from src.llm.extract_cfg import EXTRACTION_PROMPT, FORMAT_INSTRUCTIONS_KEY, TEXT_KEY
from src.models import IPDCData, IPDCCondition, IPDCCost

LLM = OllamaLLM(model='mistral-nemo', base_url='ollama.hackathon-ai-8.s.redhost.be', temperature=0.0)

def _create_pydantic_chain(pydantic_object: Type[BaseModel], prompt: str):
    output_parser = PydanticOutputParser(pydantic_object=pydantic_object)
    prompt_template = PromptTemplate.from_template(template=prompt, partial_variables={FORMAT_INSTRUCTIONS_KEY: output_parser.get_format_instructions()})
    return prompt_template | LLM | output_parser

def extract_ipdc_conditions(text: str) -> IPDCCondition:
    extract_chain = _create_pydantic_chain(pydantic_object=IPDCCondition, prompt=EXTRACTION_PROMPT)
    return extract_chain.invoke({TEXT_KEY: text})

def extract_ipdc_costs(text: str) -> IPDCCost:
    extract_chain = _create_pydantic_chain(pydantic_object=IPDCCost, prompt=EXTRACTION_PROMPT)
    return extract_chain.invoke({TEXT_KEY: text})

def extract_ipdc_data(text: str) -> IPDCData:
    ipdc_data = IPDCData(
        costs=extract_ipdc_costs(text=text),
        conditions=extract_ipdc_conditions(text=text)  
    )
    return ipdc_data

