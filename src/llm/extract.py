import os
import asyncio
from langchain_ollama.llms import OllamaLLM
from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser
from typing import Type, List
from langchain_core.prompts import PromptTemplate
from src.llm.extract_cfg import EXTRACTION_PROMPT, FORMAT_INSTRUCTIONS_KEY, TEXT_KEY
from src.models import IPDCData, IPDCProcedure, IPDCCostData, IPDCConditionData, IPDCEntry, IPDCCost, IPDCCondition
from src.models_simplified import IPDCInformationToExtract
import aiohttp
from functools import partial


def _load_llm():
    return OllamaLLM(model='mistral-nemo', base_url=os.getenv("OLLAMA_URI"), temperature=0.0)


def _create_pydantic_chain(pydantic_object: Type[BaseModel], prompt: str):
    llm = _load_llm()
    output_parser = PydanticOutputParser(pydantic_object=pydantic_object)
    prompt_template = PromptTemplate.from_template(template=prompt, partial_variables={FORMAT_INSTRUCTIONS_KEY: output_parser.get_format_instructions()})
    return prompt_template | llm | output_parser


def extract_ipdc_conditions(text: str) -> IPDCConditionData:
    extract_chain = _create_pydantic_chain(pydantic_object=IPDCConditionData, prompt=EXTRACTION_PROMPT)
    return extract_chain.invoke({TEXT_KEY: text})


def extract_ipdc_costs(text: str) -> IPDCCostData:
    extract_chain = _create_pydantic_chain(pydantic_object=IPDCCostData, prompt=EXTRACTION_PROMPT)
    return extract_chain.invoke({TEXT_KEY: text})


def extract_base_ipdc_data(text: str) -> IPDCData:
    extract_chain = _create_pydantic_chain(pydantic_object=IPDCData, prompt=EXTRACTION_PROMPT)
    return extract_chain.invoke({TEXT_KEY: text})


def extract_ipdc_procedure(text: str) -> IPDCProcedure:
    extract_chain = _create_pydantic_chain(pydantic_object=IPDCProcedure, prompt=EXTRACTION_PROMPT)
    return extract_chain.invoke({TEXT_KEY: text})


def extract_ipdc_information_simple(text: str) -> IPDCInformationToExtract:
    extract_chain = _create_pydantic_chain(pydantic_object=IPDCInformationToExtract, prompt=EXTRACTION_PROMPT)
    return extract_chain.invoke({TEXT_KEY: text})


async def call_classifier(uri: str, text: str) -> List[str]:
    body = {
        'description': text
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(uri, json=body) as response:
            data = await response.json()
            return [pred['label'] for pred in data.get("prediction", [])]



async def run_in_thread(sync_function, *args, **kwargs):
    loop = asyncio.get_running_loop()
    sync_function_noargs = partial(sync_function, *args, **kwargs)
    return await loop.run_in_executor(None, sync_function_noargs)


async def extract_ipdc_data(text: str) -> IPDCEntry:
    ipdc_information: IPDCInformationToExtract = await run_in_thread(extract_ipdc_information_simple, text=text)
    theme, tpe, doelgroep = await asyncio.gather(
        call_classifier(os.getenv("THEME_CLASSIFIER_URI"), ipdc_information.description),
        call_classifier(os.getenv("TYPE_CLASSIFIER_URI"), ipdc_information.description),
        call_classifier(os.getenv("DOELGROEP_CLASSIFIER_URI"), ipdc_information.description)
    )

    costs = [IPDCCost(description=ipdc_information.costs, name=None)]
    conditions = [IPDCCondition(description=ipdc_information.conditions, proof=None, name=None)]
    procedures = [IPDCProcedure(description=ipdc_information.procedures, name=None)]
    ipdc_data = IPDCEntry(
        description=ipdc_information.description,
        name=ipdc_information.title,
        procedure=procedures,
        cost=costs,
        condition=conditions,
        theme=theme,
        type=tpe,
        doelgroep=doelgroep
    )
    return ipdc_data
