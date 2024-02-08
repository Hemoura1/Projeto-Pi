from tkinter import filedialog
from tkinter import *
import pygame
import os

root = Tk()
root.title('Player de musica')
root.geometry("500x300")

pygame.mixer.init()

menubar = Menu(root)

root.config(menu=menubar)

musicas = []
musica_tocar = ""
paused = False

def ler_musica():
    global musica_tocar
    root.diretorio = filedialog.askdirectory()

    for musica in os.listdir(root.diretorio): 
        name, ext = os.path.splitext(musica)
        if ext == '.mp3' or ext == '.mp4':
            musicas.append(musica)

    for musica in musicas:
        listam.insert("end",musica)
    
    listam.selection_set(0)
    musica_tocar = musicas[listam.curselection()[0]]

def tocar_musica():
    global musica_tocar,paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.diretorio, musica_tocar))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False


def pause_musica():
    global paused
    pygame.mixer.music.pause()
    paused = True

def next_musica():
    global musica_tocar, paused
    try:
        listam.selection_clear(0,END)
        listam.selection_set(musicas.index(musica_tocar) + 1)
        musica_tocar = musicas[listam.curselection()[0]]
        tocar_musica()
    except:
        pass

def prev_musica():
    global musica_tocar,paused

    try:
        listam.selection_clear(0,END)
        listam.selection_set(musicas.index(musica_tocar) - 1)
        musica_tocar = musicas[listam.curselection()[0]]
        tocar_musica()
    except:
        pass
    


org_menu = Menu(menubar,tearoff=False)
org_menu.add_command(label='Selecionar Pasta', command=ler_musica)
menubar.add_cascade(label= 'Organizar', menu=org_menu)

listam = Listbox(root, bg="Black", fg="White", width=100, height=15)
listam.pack()

play_btn_imagem = PhotoImage(file='projeto/imagens/play.png')
pause_btn_imagem = PhotoImage(file='projeto/imagens/pause.png')
next_btn_imagem = PhotoImage(file='projeto/imagens/next.png')
previous_btn_imagem = PhotoImage(file='projeto/imagens/previous.png')

control_frame  = Frame(root)

control_frame.pack()

play_btn = Button(control_frame,image=play_btn_imagem,borderwidth=0, command=tocar_musica)
pause_btn = Button(control_frame,image=pause_btn_imagem,borderwidth=0, command=pause_musica)
next_btn = Button(control_frame,image=next_btn_imagem,borderwidth=0, command=next_musica)
previous_btn = Button(control_frame,image=previous_btn_imagem,borderwidth=0, command=prev_musica)

play_btn.grid(row = 0,column=2,padx=7,pady=10)
pause_btn.grid(row = 0,column=1,padx=7,pady=10)
next_btn.grid(row = 0,column=3,padx=7,pady=10)
previous_btn.grid(row = 0,column=0,padx=7,pady=10)

root.mainloop()