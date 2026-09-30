def analyze_complexity(prompt: str) -> str:
    """
    Analyzes the prompt complexity based on transparent rules:
    - prompt length
    - coding/reasoning requirements
    - mathematical difficulty
    - keywords such as analyze, optimize, architecture, debug, compare, design
    Returns 'low' or 'medium'.
    """
    text = prompt.lower()
    
    # Rule 1: Keywords for medium complexity
    medium_keywords = ["analyze", "optimize", "architecture", "debug", "compare", "design", "code", "python", "javascript", "react", "fastapi"]
    if any(keyword in text for keyword in medium_keywords):
        return "medium"
        
    # Rule 2: Math/Equation difficulty
    math_keywords = ["calculate", "equation", "formula", "derivative", "integral", "matrix"]
    if any(keyword in text for keyword in math_keywords):
        return "medium"
        
    # Rule 3: Prompt length
    # Let's say if it's more than 50 words or 300 characters, it's medium
    if len(text) > 300 or len(text.split()) > 50:
        return "medium"
        
    # Default fallback
    return "low"
