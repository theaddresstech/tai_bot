from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

from ollama_client import query_ollama
from stt import transcribe_audio
from tts import speak_text

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

os.makedirs("temp_audio", exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def get_chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

import time

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("✅ WebSocket connection opened")
    try:
        while True:
            user_input = await websocket.receive_text()
            print(f"📥 Received: {user_input}")

            start = time.time()
            bot_reply = query_ollama(user_input)
            duration = time.time() - start

            print(f"📤 Reply: {bot_reply}")
            print(f"🧠 LLM response time: {duration:.2f} seconds")

            await websocket.send_text(f"🤖 {bot_reply}")
    except WebSocketDisconnect:
        print("❌ WebSocket disconnected")


@app.post("/stt")
async def speech_to_text(file: UploadFile = File(...)):
    file_location = f"temp_audio/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    start = time.time()
    text = transcribe_audio(file_location)
    duration = time.time() - start

    print(f"📝 Transcribed: {text}")
    print(f"🎙️ STT response time: {duration:.2f} seconds")

    return {"text": text}

@app.post("/tts")
async def text_to_speech(text: str = Form(...)):
    if not text.strip():
        return {"error": "No text provided for TTS."}

    start = time.time()
    audio_path = speak_text(text)
    duration = time.time() - start

    print(f"🔊 Audio saved to {audio_path}")
    print(f"🗣️ TTS response time: {duration:.2f} seconds")

    if not os.path.exists(audio_path) or os.path.getsize(audio_path) == 0:
        return {"error": "TTS failed to generate audio."}

    return FileResponse(audio_path, media_type="audio/mpeg")




@app.get("/test")
async def test():
    return HTMLResponse("<h1>FastAPI is working ✅</h1>")
