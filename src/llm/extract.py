from langchain_ollama.llms import OllamaLLM
from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser
from typing import Type
from langchain_core.prompts import PromptTemplate
from src.llm.extract_cfg import EXTRACTION_PROMPT, FORMAT_INSTRUCTIONS_KEY, TEXT_KEY
from src.models import IPDCData, IPDCProcedure, IPDCCostData, IPDCConditionData, IPDCEntry, IPDCCost, IPDCCondition, IPDCProof

LLM = OllamaLLM(model='mistral-nemo', base_url='ollama.hackathon-ai-8.s.redhost.be', temperature=0.0)

def _create_pydantic_chain(pydantic_object: Type[BaseModel], prompt: str):
    output_parser = PydanticOutputParser(pydantic_object=pydantic_object)
    prompt_template = PromptTemplate.from_template(template=prompt, partial_variables={FORMAT_INSTRUCTIONS_KEY: output_parser.get_format_instructions()})
    return prompt_template | LLM | output_parser


def extract_ipdc_conditions(text: str) -> IPDCConditionData:
    extract_chain = _create_pydantic_chain(pydantic_object=IPDCConditionData, prompt=EXTRACTION_PROMPT)
    return extract_chain.invoke({TEXT_KEY: text})


def extract_ipdc_costs(text: str) -> IPDCCostData:
    extract_chain = _create_pydantic_chain(pydantic_object=IPDCCostData, prompt=EXTRACTION_PROMPT)
    return extract_chain.invoke({TEXT_KEY: text})


def extract_base_ipdc_data(text: str) -> IPDCData:
    extract_chain = _create_pydantic_chain(pydantic_object=IPDCConditionData, prompt=EXTRACTION_PROMPT)
    return extract_chain.invoke({TEXT_KEY: text})


def extract_ipdc_procedure(text: str) -> IPDCProcedure:
    extract_chain = _create_pydantic_chain(pydantic_object=IPDCProcedure, prompt=EXTRACTION_PROMPT)
    return extract_chain.invoke({TEXT_KEY: text})


def extract_ipdc_data(text: str) -> IPDCEntry:
    base_ipdc_data = extract_base_ipdc_data(text=text)
    procedure = extract_ipdc_procedure(text=text)
    cost_data = extract_ipdc_costs(text=text)
    condition_data = extract_ipdc_conditions(text=text)
    costs = []
    if cost_data.costs is not None:
        costs = [IPDCCost(description=c, name=None) for c in cost_data.costs]
    conditions = []
    if condition_data.conditions is not None:
        conditions = [IPDCCondition(description=c, proof=None, name=None) for c in condition_data.conditions]
    ipdc_data = IPDCEntry(
        description=base_ipdc_data.description,
        name='',
        procedure=[procedure],
        cost=costs,
        condition=conditions  
    )
    return ipdc_data
