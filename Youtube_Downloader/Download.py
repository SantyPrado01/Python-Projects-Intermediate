from pytube import YouTube
from tkinter import *
from tkinter import messagebox as Messagebox

def action():
    link = videos.get()
    video = YouTube(link)
    download = video.streams.get_highest_resolution()
    download.download()

def popup():
    Messagebox.showinfo('Informacion', 'Mi perfil de linkedin: https://www.linkedin.com/in/santiago-prado-a03631228/')


root = Tk()
root.config(bd=15)
root.iconbitmap("youtube.ico")

root.title('YouTube Dowload')

walppaper = PhotoImage(file = 'youtube.png')
cambio_img = walppaper.subsample(2,2)

image = Label(root, image=cambio_img)
image.grid(row=0, column=0)


menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_command(label= 'Informacion', command=popup)

instructions = Label(root, text = 'Ingresa el Url del video a descargar', font=('Arial',15))
instructions.grid(row=1, column=0)

videos = Entry(root)
videos.grid(row=2, column=0, pady=5, padx=20, ipadx=20, ipady=5)

boton_download = Button(root, text = 'Descargar', command = action, width=10, height=2)
boton_download.grid(row=3, column=0)

root.mainloop()
 