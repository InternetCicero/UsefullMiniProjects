import os
from tkinter import * 
from pytube import YouTube
from tkinter import ttk

#ablage = input("Ablage Ordner: ")

#GUI initiieren
root = Tk()
root.geometry('500x300') 
root.resizable(0, 0) 
root.title('youtube downloader')

#Labels und Eingabefeld des GUI
lb = Label(root, text="Download YouTube Videos/Audio", font='san-serif 16 bold').pack()
link = StringVar() 
lb = Label(root, text="Paste your link here", font='san-serif 15 bold').place(x=150, y=55)
link_enter = Entry(root, width=70, textvariable=link).place(x=30, y=85)

def MP3(): #--> Für Audio

    try:
        #Adio Downloaden
        url = YouTube(str(link.get())) 
        audio = url.streams.filter(only_audio=True).first() #Filtern nach nur Audio
        download_file = audio.download() #--> Für Ablage Ordner (output_path=ablage)
        name_of_download, file_format = os.path.splitext(download_file)

        #Zur .mp3 Datei umwandeln    
        final_file = f'{name_of_download}.mp3'
        os.rename(download_file, final_file)

        a = Label(root, text="Donwload fertig!", font="arial 15")
        a.place(x=175, y=120)
        a.pack()
        root.after(1500, lambda: a.destroy())

    except:
        #Falls keine mögliche eingame Vorhanden
        a = Label(root, text="Keine mögliche Eingabe vorhanden!", font="arial 15")
        a.place(x=175, y=120)
        a.pack()
        root.after(1500, lambda: a.destroy())


def MP4(): #--> Für Video

    try: 
        #Download
        url = YouTube(str(link.get())) 
        video = url.streams.get_highest_resolution()
        download_file = video.download()

        #Keine umbennung nötig, da bereits MP4 Format


        a = Label(root, text="Download fertig!", font="arial 15")
        a.place(x=175, y=120)
        a.pack()
        root.after(1500, lambda: a.destroy())

    except:
        #Falls keine mögliche Eingabe vorhanden
        a = Label(root, text="Keine mögliche Eingabe vorhanden!", font="arial 15")
        a.place(x=175, y=120)
        a.pack()
        root.after(1500, lambda: a.destroy())


#Buttons
Button(root, text='MP4', font='san-serif 16 bold', bg='red', padx=2, command=MP4).place(x=150, y=150)
Button(root, text='MP3', font='san-serif 16 bold', bg='red', padx=2, command=MP3).place(x=250, y=150)


root.mainloop()
