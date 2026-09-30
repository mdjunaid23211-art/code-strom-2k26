from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from router.complexity import analyze_complexity
from router.routing_engine import route_request
from models.ollama_client import generate_response

router = APIRouter()

class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    response: str
    selected_model: str
    complexity: str
    latency_ms: float

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    if not request.prompt or not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")

    prompt = request.prompt
    
    # 1. Analyze complexity
    complexity = analyze_complexity(prompt)
    
    # 2. Select appropriate model based on complexity
    selected_model = route_request(complexity)
    
    # 3. Call Ollama
    try:
        response_text, latency = await generate_response(prompt, selected_model)
    except ConnectionError:
        raise HTTPException(status_code=503, detail="Ollama service is unavailable.")
    except ValueError as e:
        # e.g., model not found
        raise HTTPException(status_code=404, detail=str(e))
    except TimeoutError:
        raise HTTPException(status_code=504, detail="Request to Ollama timed out.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

    return ChatResponse(
        response=response_text,
        selected_model=selected_model,
        complexity=complexity,
        latency_ms=latency
    )
