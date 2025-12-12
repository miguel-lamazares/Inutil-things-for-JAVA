import os
import subprocess
import sys
import asc

def print_progress_bar(current, total, bar_length=20):
    progress = current / total
    filled_length = int(bar_length * progress)
    bar = '∎' * filled_length + '.' * (bar_length - filled_length)
    sys.stdout.write(f'\r[{bar}] {current}/{total}')
    sys.stdout.flush()
    if current == total:
        print()

asc.typewrite(asc.Colors.PURPLE + "Configure your jp2a\n", 0.1)
asc.typewrite(asc.Colors.GREEN + "Colors\n\n", 0.05)
asc.typewrite(asc.Colors.CYAN + "1. Real colors\n2. Black and white\n3. Manual config\n", 0.05)

colors = asc.read_int(3)

# ---------------------------------------------
# CONFIG JP2A
# ---------------------------------------------
if colors == 1:
    jp2a_cmd = ["jp2a", "--invert", "--colors", "--color-depth=24"]
elif colors == 2:
    jp2a_cmd = ["jp2a"]  # default: B/W
elif colors == 3:
    asc.typewrite("Red   (0.0 a 1.0): ", 0.1)
    red = input()
    asc.typewrite("Green (0.0 a 1.0): ", 0.1)
    green = input()
    asc.typewrite("Blue  (0.0 a 1.0): ", 0.1)
    blue = input()

    jp2a_cmd = [
        "jp2a",
        "--colors",
        "--color-depth=24",
        f"--red={red}",
        f"--green={green}",
        f"--blue={blue}"
    ]
else:
    print("Invalid option.")
    exit()

folder = "/home/dex/Documentos/GitHub/Inutil-things-for-JAVA/Gif/Gif to frames/Frame in png/"

png_files = [f for f in sorted(os.listdir(folder)) if f.endswith(".png")]
max_frames = len(png_files)

asc_frames = []

# ---------------------------------------------
# GENERATE ASCII FRAMES
# ---------------------------------------------
for i, filename in enumerate(png_files):
    path = os.path.join(folder, filename)

    result = subprocess.run(jp2a_cmd + [path], capture_output=True, text=True)

    # keep ANSI SAFE!!!
    frame = result.stdout

    asc_frames.append(frame)

    print_progress_bar(i + 1, max_frames)

# ---------------------------------------------
# SAVE art.java
# ---------------------------------------------
with open("../Loop/cave/AscFrames/art.java", "w", encoding="utf-8") as f:
    f.write("package Gif.Loop.cave.AscFrames;\n\npublic class art {\n\n")

    for i, frame in enumerate(asc_frames):

        # escape ONLY what Java needs:
        escaped = frame.replace("\\", "\\\\").replace("\"", "\\\"").replace("\n", "\\n")

        f.write(f'    public static String frame{i} = "{escaped}";\n\n')

    f.write("}\n")

# ---------------------------------------------
# SAVE aray.java
# ---------------------------------------------
with open("../Loop/cave/AscFrames/aray.java", "w", encoding="utf-8") as f:
    f.write("package Gif.Loop.cave.AscFrames;\n\npublic class aray {\n")
    f.write("    public static String[] frames = {\n")

    for i in range(max_frames):
        sep = "," if i < max_frames - 1 else ""
        f.write(f"        art.frame{i}{sep}\n")

    f.write("    };\n}\n")

print("\nFile aray.java and art.java were made with success!")
