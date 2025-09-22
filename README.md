# 🧠 Tai_Bot — Real-Time Voice Chat Assistant

Tai_Bot is a real-time, voice-enabled chatbot powered by open-source AI models. It supports both text and speech input, generates intelligent responses using a local LLM (via Ollama), and replies with synthesized speech. Designed for modular deployment and natural interaction, Tai_Bot is ideal for building conversational agents in Egyptian Arabic or any language you choose.

---

## 🚀 Features

- ✅ Real-time chat via WebSocket  
- 🔊 Text-to-speech (TTS) using `pyttsx3`  
- 🎙️ Speech-to-text (STT) using Whisper  
- 🧠 Local LLM integration via Ollama (e.g., LLaMA3)  
- 🎤 Voice input with browser microphone recording  
- 🗣️ Voice output with audio playback  
- 🧩 Modular backend using FastAPI  
- 📱 Responsive frontend with avatars and status tracking  
- 🌐 Fully offline capable (no cloud dependencies)

---

## 🧰 Tech Stack

| Layer     | Tools Used                     |
|-----------|--------------------------------|
| Frontend  | HTML, JavaScript, CSS          |
| Backend   | FastAPI, Uvicorn               |
| TTS       | pyttsx3                        |
| STT       | Whisper (via `openai-whisper`) |
| LLM       | Ollama (local model serving)   |
| Audio     | Web Audio API, MediaRecorder   |

---

## 📦 Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Start Ollama server
ollama serve

# Pull your model (e.g., LLaMA3)
ollama pull llama3

# Run FastAPI server
uvicorn main:app --reload




🌐 Usage
Open your browser and visit: http://localhost:8000

Type a message or click 🎤 Speak to record voice

Tai_Bot will reply with text and voice

Click 🔊 Voice Reply to replay the bot’s response


📁 Project Structure
tai_bot/
├── main.py               # FastAPI app
├── tts.py                # Text-to-speech logic
├── stt.py                # Speech-to-text logic
├── ollama_client.py      # LLM query logic
├── templates/
│   └── chat.html         # Frontend UI
├── static/
│   └── style.css         # Styling
├── temp_audio/           # Audio files
└── requirements.txt      # Python dependencies

