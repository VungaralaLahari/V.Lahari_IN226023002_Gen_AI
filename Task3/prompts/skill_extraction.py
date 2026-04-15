from langchain_core.prompts import PromptTemplate

skill_extraction_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""EXPERT RESUME PARSER - Extract ONLY what's WRITTEN

🚫 DO NOT assume/add skills
✅ Use EXACT terms from resume
✅ Leave empty if missing

JSON format ONLY:
{{"skills": "list,or,empty", "experience": "text,or,empty", "tools": "list,or,empty"}}

Resume:
{resume}

JSON:"""
)