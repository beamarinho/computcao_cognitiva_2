from tkinter import *


ws = Tk()
ws.geometry('400x300')
ws.title('Computação Cognitiva 2')
ws['bg'] = '#ffffff'

f = ("Times bold", 14)


def text2speech():
    ws.destroy()
    import page1


def speech2text():
    ws.destroy()
    import page2


Label(
    ws,
    text="Escolha uma opção",
    padx=20,
    pady=20,
    bg='#ffffff',
    font=f
).pack(expand=True, fill=BOTH)

Button(
    ws,
    text="Text to Speech",
    font=f,
    command=text2speech
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="Speech to text",
    font=f,
    command=speech2text
).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()


# if __name__ == "__main__":
#     ws = tk.Tk()
#     main = MainView(root)
#     main.pack(side="top", fill="both", expand=True)
#     root.wm_geometry("400x400")
#     root.mainloop()