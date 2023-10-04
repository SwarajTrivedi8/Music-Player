import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas=tk.Tk()
canvas.title("Music Player")
canvas.geometry("200x386")
canvas.config(bg="whitesmoke")



rootpath="c:\\Users\yeash\Downloads\Fred again actual life3"
pattern="*.mp3"

mixer.init()

prev_img=tk.PhotoImage(file="prev.png")
prevsmaller_image = prev_img.subsample(4, 4)
farward_img=tk.PhotoImage(file="farward.png")
farsmaller_image = farward_img.subsample(4, 4)
stop_img=tk.PhotoImage(file="stop.png")
stopsmaller_image = stop_img.subsample(4, 4)
pause_img=tk.PhotoImage(file="pause.png")
pausesmaller_image = pause_img.subsample(4, 4)
play_img=tk.PhotoImage(file="play.png")
playsmaller_image = play_img.subsample(4, 4)

def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def select1():
    if pauseButton["text"]=="pause":
        mixer.music.pause()
        pauseButton["text"]=="play"
    else:
        mixer.music.unpause()
        pauseButton["text"]=="pause"



def select2():
    nextsong=listBox.curselection()
    nextsong=nextsong[0]+1
    nextsongname=listBox.get(nextsong)
    label.config(text=nextsongname)
    mixer.music.load(rootpath + "\\" + nextsongname)
    mixer.music.play()

    listBox.select_clear(0, "end")
    listBox.activate(nextsong)
    listBox.select_set(nextsong)

def select3():
    prevsong=listBox.curselection()
    prevsong=prevsong[0]-1
    prevsongname=listBox.get(prevsong)
    label.config(text=prevsongname)
    mixer.music.load(rootpath + "\\" + prevsongname)
    mixer.music.play()

    listBox.select_clear(0, "end")
    listBox.activate(prevsong)
    listBox.select_set(prevsong)


listBox=tk.Listbox(canvas, fg="midnightblue",bg="lightblue",width=100,font=("ChicagoFLF",14))
listBox.pack(padx=15,pady=15)

label=tk.Label(canvas,text="",bg="whitesmoke",fg="midnightblue",font=("ChicagoFLF",10))
label.pack(pady=10)



top=tk.Frame(canvas,bg="black")
top.pack(padx=10,pady=1,anchor="center")

prevButton=tk.Button(canvas,text="Prev",image=prevsmaller_image,bg="whitesmoke",borderwidth=0,command=select3)
prevButton.pack(pady=.05,in_=top,side="left")

playButton=tk.Button(canvas,text="play",image=playsmaller_image,bg="whitesmoke",borderwidth=0,command=select)
playButton.pack(pady=.05,in_=top,side="left")

farButton=tk.Button(canvas,text="far",image=farsmaller_image,bg="whitesmoke",borderwidth=0,command=select2)
farButton.pack(pady=.05,in_=top,side="left")

pauseButton=tk.Button(canvas,text="pause",image=pausesmaller_image,bg="whitesmoke",borderwidth=0,command=select1)
pauseButton.pack(pady=.05,in_=top,side="left")





for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listBox.insert("end",filename)

canvas.mainloop()