import os
import subprocess

def text_to_audio(folder):
    print("TTA - ", folder)
    

def create_reel(folder):
    command="ffmpeg -f concat -safe 0 -i user_uploads/c8e32e90-2c2b-11f1-9a59-b2be6a47ff30/input.txt -i user_uploads/c8e32e90-2c2b-11f1-9a59-b2be6a47ff30/audio.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/c8e32e90-2c2b-11f1-9a59-b2be6a47ff30.mp4"
    subprocess.run(command, shell=True, check=True)

if __name__ == "__main__":
    with open("done.txt", "r") as f:
        done_folders = f.readlines()

        done_folders = [f.strip() for f in done_folders]
        folders=os.listdir("user_uploads")
        for folder in folders:
            if(folder not in done_folders):
                text_to_audio(folder) #Generate the audio.mp3 from desc.txt
                create_reel(folder) #Convert the images and audio.mp3 inside the folder to reel
                with open("done.txt", "a") as f:
                    f.write(folder + "\n")
                    