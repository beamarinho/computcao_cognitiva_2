import assets
from tkinter import *
principal = Tk()
principal.title("Computação Cognitiva 2")
principal.geometry('400x300')
principal.rowconfigure(0, minsize=800, weight=1)
principal.columnconfigure(1, minsize=800, weight=1)
principal['bg']='#B3B6B7'

f = ("Times bold", 12)


micro = PhotoImage(file = r"assets/micro.png")
micro.transparency_set(1,1)
microImg = micro.subsample(10)

Label(
    principal,
    text="Escolha uma opção",
    padx=20,
    pady=20,
    bg='#B3B6B7',
    font=f
).pack(expand=True, fill=BOTH)

Button(
    principal, 
    text="Txt to Speech",
    padx=20,
    pady=20,
    font=f,
    image=microImg,
    compound=LEFT
    ).pack(fill=X,expand=TRUE, side=LEFT)
Button(
    principal, 
    text="Speech to Txt", 
    font=f,
    padx=20,
    pady=20,
    image=microImg,
    compound=LEFT
    ).pack(fill=X,expand=TRUE, side=LEFT)


principal.mainloop()


def txtToSpeechPage():
    principal.destroy()
    import paginaTexto

def speechToTxtPage():
    principal.destroy()
    import paginaAudio