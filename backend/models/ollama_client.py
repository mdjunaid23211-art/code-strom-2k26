import os
import time
import httpx
from typing import Tuple

async def generate_response(prompt: str, model_name: str) -> Tuple[str, float]:
    """
    Sends the prompt to the local Ollama API and returns the generated response 
    along with the latency in milliseconds.
    """
    ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434")
    
    # We use httpx.AsyncClient for async HTTP requests
    start_time = time.time()
    
    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                f"{ollama_url}/api/generate",
                json={
                    "model": model_name,
                    "prompt": prompt,
                    "stream": False
                }
            )
            
            # Check for HTTP errors
            if response.status_code == 404:
                raise ValueError(f"Model '{model_name}' not found on Ollama server.")
            elif response.status_code != 200:
                raise Exception(f"Ollama API error: {response.text}")
                
            data = response.json()
            response_text = data.get("response", "")
            
    except httpx.ConnectError:
        raise ConnectionError("Failed to connect to Ollama.")
    except httpx.TimeoutException:
        raise TimeoutError("Ollama request timed out.")
        
    end_time = time.time()
    latency_ms = (end_time - start_time) * 1000.0
    
    return response_text, latency_ms
