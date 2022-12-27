from tkinter import *
from pygame import mixer
import os

root = Tk()

root.resizable(0,0)

root.title('Music Player')

def play():
    currentsong = playlist.get(ACTIVE)
    mixer.music.load(currentsong)
    mixer.music.play()

def pause():
    mixer.music.pause()

def resume():
    mixer.music.unpause()

def stop():
    mixer.music.stop()

mixer.init()

playlist = Listbox(root, selectmode=SINGLE, bg="white", fg="black", font=('arial', 15), width=30)
playlist.grid(columnspan=12)

os.chdir = os.chdir(r"E:\MUSIC PLAYER\songs")
songs = os.listdir()

for s in songs:
    playlist.insert(END, s)

playbtn = Button(root, text="Play" , command=play, bg='yellow', fg='blue')
playbtn.grid(row=1, column = 0)

pausebtn = Button(root, text="Pause" , command=pause, bg='yellow', fg='red')
pausebtn.grid(row=1, column = 4)

Resumebtn = Button(root, text="Resume" , command=resume, bg='yellow', fg='green')
Resumebtn.grid(row=1, column = 7)

stopbtn = Button(root, text="stop" , command=stop, bg='yellow', fg='black')
stopbtn.grid(row=1, column = 10)

mainloop()



