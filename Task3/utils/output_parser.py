def parse_extraction_json(text: str) -> dict:
    """Simple JSON-like parser for extracted skills"""
    try:
        # Extract JSON-like structure
        if '{' in text and '}' in text:
            json_part = text.split('{', 1)[1].split('}', 1)[0]
            parts = json_part.split(',')
            return {
                "skills": parts[0].split(':')[1].strip().strip('"') if len(parts) > 0 else "",
                "experience": parts[1].split(':')[1].strip().strip('"') if len(parts) > 1 else "",
                "tools": parts[2].split(':')[1].strip().strip('"') if len(parts) > 2 else ""
            }
        return {"skills": "", "experience": "", "tools": ""}
    except:
        return {"skills": "", "experience": "", "tools": ""}

def parse_score_output(text: str) -> dict:
    """Parse score output"""
    score_line = [line for line in text.split('\n') if 'Score:' in line]
    explanation_lines = [line for line in text.split('\n') if 'Explanation:' in line]
    
    return {
        "score": score_line[0].split('Score:')[1].strip() if score_line else "N/A",
        "explanation": explanation_lines[0].replace('Explanation:', '').strip() if explanation_lines else "No explanation",
        "raw": text[:200] + "..." if len(text) > 200 else text
    }