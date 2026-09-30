import os
from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.chat import router as chat_router
import httpx

app = FastAPI(title="LLM Cost-Quality Routing Fabric Backend")

# Allow CORS for the React frontend (Vite uses 5173 by default)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "*"],  # allow * for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api")

@app.get("/api/health")
async def health_check():
    ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434")
    ollama_status = "unavailable"
    
    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            response = await client.get(f"{ollama_url}/api/version")
            if response.status_code == 200:
                ollama_status = "available"
    except Exception:
        pass
        
    return {
        "backend": "available",
        "ollama": ollama_status
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
