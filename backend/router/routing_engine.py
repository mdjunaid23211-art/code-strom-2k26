from router.model_registry import LOW_COMPLEXITY_MODEL, MEDIUM_COMPLEXITY_MODEL, HIGH_COMPLEXITY_MODEL

def route_request(complexity: str) -> str:
    """
    Selects the appropriate Ollama model based on the analyzed complexity.
    """
    if complexity == "low":
        return LOW_COMPLEXITY_MODEL
    elif complexity == "medium":
        return MEDIUM_COMPLEXITY_MODEL
    elif complexity == "high":
        # For future extension
        return HIGH_COMPLEXITY_MODEL
    
    # Fallback to low complexity
    return LOW_COMPLEXITY_MODEL
