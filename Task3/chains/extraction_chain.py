from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from prompts.skill_extraction import skill_extraction_prompt

def create_extraction_chain():
    """FREE HuggingFace LLM Chain"""
    # FREE model - no API key needed
    llm = HuggingFaceEndpoint(
        repo_id="microsoft/DialoGPT-medium",
        temperature=0.1,
        max_new_tokens=200,
        huggingfacehub_api_token=None  # FREE
    )
    
    chain = (
        {"resume": skill_extraction_prompt} 
        | llm 
        | StrOutputParser()
    )
    
    return chain