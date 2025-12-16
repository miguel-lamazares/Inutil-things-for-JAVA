# -----------------------------
# C build
# -----------------------------
gcc "./Gif/Render/Render.c" -O3 -o "./Gif/Render/Render"

# -----------------------------
# Java build
# -----------------------------
javac "./Gif/Player/gif.java"

# -----------------------------
# Run animation
# -----------------------------
java Gif.Player.gif
