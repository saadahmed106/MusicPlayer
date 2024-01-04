from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os


root=Tk()
root.geometry("920x670+290+85")
root.title("Music Player ")
root.configure(bg="#800000")
root.resizable(False, False)


mixer.init()
def open_folder():
    path=filedialog.askdirectory()

    if path:
        os.chdir(path)

        songs=os.listdir(path)

    for i in songs:
        if i.endswith(".mp3"):
            playerlist.insert(END, i)
def player_song():
    music_name=playerlist.get(ACTIVE)

    mixer.music.load(playerlist.get(ACTIVE))

    mixer.music.play()
    music.config(text=music_name[0:-4])

image_icon=PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

top=PhotoImage(file="top (1).png")
Label(root,image=top,bg="#800000").pack()

logo=PhotoImage(file="logo.png")
Label(root,image=logo,bg="#800000").place(x=64,y=115)

play_button=PhotoImage(file="play.png")
Button(root,image=play_button,bg="#800000",bd=0,activebackground="black",).place(x=100,
y=400)
stop_button=PhotoImage(file="stop.png")

Button(root,image=stop_button,bg="#800000",bd=0, activebackground="black", command=mixer.music.stop).place(x=30,y=500)


resume_button=PhotoImage(file="resume.png")

Button(root, image=resume_button,bg="#800000",bd=0, activebackground="black",command=mixer.music.unpause).place(x=115,
y=500)



pause_button=PhotoImage(file="pause.png")

Button(root, image=pause_button,bg="#800000",bd=0, activebackground="black",command=mixer.music.pause).place(x=200,
y=500)





music=Label(root, text="", font=("arial 15"), fg="white",bg="#800000")
music.place(x=150, y=340, anchor="center")


Menu=PhotoImage(file="menu.png")

Label(root, image=Menu, bg="#800000",bd=0).pack(padx=10, pady=10,side=RIGHT)



Music_frame=Frame(root, bd=2, relief=RIDGE)
Music_frame.place(x=330, y=350, width=560, height=250)


(Button(root, text="Open Folder", width=15, height=2, font=("arial 10 bold"), fg="red",bg="cyan",

command=open_folder).place(x=330,y=300))


scroll=Scrollbar(Music_frame)

playerlist=Listbox(Music_frame, width=100, font=("arial 10"), bg="#333333",fg="gray",selectbackground="lightblue",
 cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playerlist.yview)

scroll.pack(side=RIGHT, fill=Y)

playerlist.pack(side=LEFT, fill=BOTH)

root.mainloop()
