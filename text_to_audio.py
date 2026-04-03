import os
import uuid
from gtts import gTTS

def text_to_speech_file(text: str, folder: str) -> str:
    save_folder = os.path.join("user_uploads", folder)
    os.makedirs(save_folder, exist_ok=True)

    file_path = os.path.join(save_folder, "audio.mp3")  # ✅ FIXED NAME

    tts = gTTS(text=text, lang='en')
    tts.save(file_path)

    print(f"{file_path}: Audio file saved successfully!")
    return file_path


# Test run
if __name__ == "__main__":
    pass
   # text_to_speech_file(
   #     "Hey I am good girl and this is my Python project",
   #     "test_folder"
   # )