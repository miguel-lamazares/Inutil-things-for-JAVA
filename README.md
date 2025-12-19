# Gif to ASC II 🎥

This simple project makes your terminal show gifs as ASC II arts.

## Architecture
#### Python 🐍
* the file ```8.py```, it's the responsibly for trasforming the gifs to frames, these frames are saved in ```Frame in png``` folder.
* the file ```JP2a.py```, it's the responsibly for taking those frames and trasform them in ASCII arts with user's configs such as size, colors, etc. After transforming some freme in ASC, it saves that in two java files.
* the file ```asc.py```, it's a form to let it more cool with small animations, colors, clear the terminal and error processing.

#### Java ☕
* ```gif.java``` makes the magic, taking all frames and making them behave as GIF, how? anything that it's animated, in reality it's an illution of moviment, just frames being showed sequencily, it's just show a frame and clean it and show another.
*  ```aray.java```, it's made by ```JP2a.py```, the script reads the folder and with the index write the number of frames doing refence at other files.
*  ```art.java```, this long achive is the heart of program, but it has a problem with optimization, because all frames are there. Anyways, this is made too by ```JP2a.py```, all frames were enumeted for the number of png that it will convert.

#### Shell 🐚
* ```start.sh```, it's a compile of commands as start scripts and copile the java and start it.

#### Docker 🐳
* it unites everthing that you will need the jdk, python and jp2a.

## How it works

<img src="">
