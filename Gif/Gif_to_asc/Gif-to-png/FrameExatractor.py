from PIL import Image
import os

import shutil
from TerminalLib import asc

print("\033[H\033[2J", flush=True)

output_dir = "./Gif/Gif_to_asc/Frame in png"
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

xz = input("what's the GIF's address?: ")

if xz.startswith("https:"):
    folder = "Gif/Gif_to_asc/Gif-to-png/Downloads"
    asc.download(xz, folder)
    xz = f"{folder}/gif.gif"

elif xz.startswith("http:"):
    folder = "Gif/Gif_to_asc/Gif-to-png/Downloads"
    asc.download(xz, folder)
    xz = f"{folder}/gif.gif"

        

gif = Image.open(xz)
for i in range(gif.n_frames):
    gif.seek(i)
    gif.save(f"{output_dir}/frame_{i}.png")
    
    asc.print_progress_bar(i + 1, gif.n_frames)

