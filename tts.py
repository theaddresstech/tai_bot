import pyttsx3
import os
import time

def speak_text(text: str, output_file: str = "response.mp3") -> str:
    output_path = os.path.join("temp_audio", output_file)
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()


    # Wait until file is fully written
    for _ in range(10):
        if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
            break
        time.sleep(0.2)


    return output_path
