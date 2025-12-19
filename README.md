# Gif to ASC II 🎥

This simple project makes your terminal show gifs as ASC II arts.

## Architecture 
### What I Used and Why
#### Python 🐍
Responsible for managing files, transforming GIFs into frames, and converting them into ASCII art using JP2A.
#### TerminalLib 🏞️
A custom library used to make the terminal more user-friendly and error-free, avoiding unnecessary prompts (e.g., "how old are you?").

#### Java ☕
The heart of the project. It controls the terminal, orchestrates C, manages screen timing, and shares the correct file with C.

#### C ⚙️
Acts as a graphics engine. It handles the heavy lifting, printing and clearing large strings.

#### Shell 🐚
All commands compiled into three forms:

* Full process: Provide the GIF and configs before starting.
* Just the GIF address: No config needed, uses the last saved config to start.
* Execute only: Runs the GIF in memory (or the last loaded GIF).

#### Docker 🐳
The project image for easier use, including JDK, libraries, Python, GCC, and all necessary commands.

## How it works
<div align="center"  justify-content="center">
<p></p>
  <img src="./howItWorks.svg">
</div>

