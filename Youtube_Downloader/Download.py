from pytube import YouTube
from tkinter import *
from tkinter import messagebox as Messagebox

def action():
    link = videos.get()
    video = YouTube(link)
    download = video.streams.get_highest_resolution()
    download.download()
def popup():
    Messagebox.showinfo('About my', 'Link to my linkedin profile: https://www.linkedin.com/in/santiago-prado-a03631228/')


root = Tk()
root.config(bd=15)
root.title('YouTube Dowload')

walppaper = PhotoImage(file = 'Download_Youtube\YouTube.png', width = 60, height = 40)
image = Label(root, image=walppaper, bd=0)
image.grid(row=0, column=0)


menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)


menubar.add_command(label= 'Author Information', command=popup)
menubar.add_command(label= 'Exit', command = root.destroy)

instructions = Label(root, text = 'Program created to download videos from youtube\n')
instructions.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

boton_download = Button(root, text = 'Download', command = action)
boton_download.grid(row=2, column=1)

root.mainloop()
 