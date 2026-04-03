import os
import subprocess
from text_to_audio import text_to_speech_file

def create_reel(folder):
    input_path = "input.txt"
    audio_path = "audio.mp3"
    output_path = f"../../static/reels/{folder}.mp4"

    command = f"""ffmpeg -f concat -safe 0 -i {input_path} -i {audio_path} \
    -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2" \
    -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest {output_path}"""

    print("Running:", command)

    subprocess.run(
        command,
        shell=True,
        check=True,
        cwd=f"user_uploads/{folder}"   # 🔥 THIS IS KEY FIX
    )
    
if __name__ == "__main__":
    if not os.path.exists("done.txt"):
        open("done.txt", "w").close()

    with open("done.txt", "r") as f:
        done_folders = [f.strip() for f in f.readlines()]

    folders = os.listdir("user_uploads")

    for folder in folders:
        if folder not in done_folders:
            print("Processing:", folder)

            # Read description
            with open(f"user_uploads/{folder}/desc.txt", "r") as f:
                text = f.read()

            # Generate audio
            text_to_speech_file(text, folder)

            # Create reel
            create_reel(folder)

            # Mark as done
            with open("done.txt", "a") as f:
                f.write(folder + "\n")