LOW_COMPLEXITY_MODEL = "qwen3:4b"
MEDIUM_COMPLEXITY_MODEL = "qwen3:8b"
# Future extensibility for high complexity
HIGH_COMPLEXITY_MODEL = "qwen3:14b"

def get_available_models():
    """
    Returns a list of models supported by the system.
    """
    return [
        LOW_COMPLEXITY_MODEL,
        MEDIUM_COMPLEXITY_MODEL,
        HIGH_COMPLEXITY_MODEL
    ]
