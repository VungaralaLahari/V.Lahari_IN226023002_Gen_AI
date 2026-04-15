from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from prompts.scoring_prompt import scoring_prompt

def create_scoring_chain():
    """FREE Scoring Chain"""
    llm = HuggingFaceEndpoint(
        repo_id="microsoft/DialoGPT-medium",
        temperature=0.1,
        max_new_tokens=150,
        huggingfacehub_api_token=None  # FREE
    )
    
    chain = (
        {
            "extracted_data": lambda x: x,
            "job_description": RunnablePassthrough()
        }
        | scoring_prompt
        | llm
        | StrOutputParser()
    )
    
    return chain