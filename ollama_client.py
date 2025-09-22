import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def query_ollama(prompt: str, model: str = "llama3") -> str:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
