#  **Mastering Dynamic Prompt Templates with LangChain**


##  Project Overview
This project demonstrates building a **Mini Prompt Engine** using **LangChain's PromptTemplate**. 

**Problem Solved**: Replace static, hardcoded prompts with **dynamic, reusable prompt systems** that generate prompts automatically based on user inputs like topic, audience, tone, and style.

**From this** ➜ `"Explain AI for beginners in a friendly tone"`  
**To this** ➜ `"Explain {topic} for {audience} in a {tone} tone"`

##  Objectives
-  Implement `PromptTemplate` for dynamic prompt generation
-  Build multi-input prompt systems (topic, audience, tone, style)
-  Create role-based `ChatPromptTemplate` (Teacher, Interviewer, Motivator)
-  Add input validation with default fallbacks
-  Design reusable prompt generator functions

##  Why This Matters
| Traditional Prompts | LangChain Prompt Engine |
|-------------------|-------------------------|
| Static & inflexible | **Dynamic & flexible** |
| Hard to reuse | **Fully reusable** |
| Manual editing | **Automated generation** |
| Not scalable | **Production-ready** |

##  Tech Stack
- **Python **
- **LangChain**
- **Jupyter Notebook / Google Colab**

##  Repository Structure
- Task1
- README.md

  
##  Tasks Completed

### Task 1: Dynamic Prompt Templates
```python
from langchain.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["topic", "audience", "tone"],
    template="Explain {topic} for {audience} in a {tone} tone"
)
```

### Task 2: Multi-Input System
**Inputs**: `topic`, `audience`, `tone`  
**Output**: `"Explain Machine Learning for beginners in a friendly tone"`

### Task 3: Prompt Variations
-  **Teaching**: "Teach {topic} to {audience} using simple examples"
-  **Interview**: "Prepare {audience} to answer {topic} interview questions"
-  **Storytelling**: "Write a story about {topic} for {audience}"

### Task 4: ChatPromptTemplate with Roles
```python
ChatPromptTemplate.from_messages([
    ("system", "You are a {role}"),
    ("user", "{input}")
])
```
**Supported Roles**: Teacher, Interviewer, Motivator

### Task 5: Input Validation
```python
def validate_input(audience, tone):
    valid_audiences = ["beginner", "intermediate", "expert"]
    valid_tones = ["formal", "casual", "fun"]
    # Returns validated inputs or defaults
```

### Task 6: Prompt Generator Function
```python
def generate_prompt(topic, audience="beginner", tone="friendly", style="teaching"):
    # Dynamic template selection + validation
    return template.format(topic=topic, audience=audience, tone=tone)
```

### Task 7: Reusability Demo
Same template → Multiple outputs:

- "Explain AI for beginners in friendly tone"
- "Explain Neural Networks for experts in formal tone"
- "Explain Data Science for intermediate in casual tone"


##  Key Learnings
- **Prompt Engineering**: Dynamic templates > hardcoded prompts
- **Modularity**: Single function handles multiple use cases
- **Validation**: Production-ready input handling
- **Scalability**: Template system works for chatbots, assistants, content generators

