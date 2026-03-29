import os
import uuid
from gtts import gTTS


def text_to_speech_file(text: str, folder: str) -> str:
    # Create folder if not exists
    save_folder = os.path.join("user_uploads", folder)
    os.makedirs(save_folder, exist_ok=True)

    # Generate unique filename
    filename = f"{uuid.uuid4()}.mp3"
    file_path = os.path.join(save_folder, filename)

    # Convert text to speech
    tts = gTTS(text=text, lang='en')

    # Save audio file
    tts.save(file_path)

    print(f"{file_path}: Audio file saved successfully!")

    return file_path


# Test run
if __name__ == "__main__":
   # text_to_speech_file(
   #     "Hey I am good girl and this is my Python project",
   #     "test_folder"
   # )