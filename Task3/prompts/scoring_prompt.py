from langchain_core.prompts import PromptTemplate

scoring_prompt = PromptTemplate(
    input_variables=["extracted_data", "job_description"],
    template="""RECRUITER SCORING - 0-100 scale

Perfect (90-100): All key skills + experience
Good (70-89): Most skills + some exp
Average (50-69): Some skills
Weak (30-49): Few skills  
Poor (0-29): No relevant skills

Format EXACTLY:
Score: <0-100>
Explanation: <WHY this score - 2 sentences>

Resume Data:
{extracted_data}

Job Req:
{job_description}

Score:"""
)