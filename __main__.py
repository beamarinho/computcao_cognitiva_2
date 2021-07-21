from pages.Page import  Page
from pages.TextPage import TxtToSpeech
from pages.AudioPage import SpeechToTxt
import tkinter as tk

class Principal(Page):
  def __init__(self, *args, **kwargs):
      Page.__init__(self,*args, **kwargs)
      label = tk.Label(self, text="Computação Cognitiva 2")
      label.pack(side="top", fill="both", expand= True)
class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        f = ("Times bold", 12) 
        p1 = Principal(self)
        p2 = SpeechToTxt(self)
        p3 = TxtToSpeech(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="bottom", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b2 = tk.Button(buttonframe, text="Text to Speech", font=f,padx=10, pady=10, command=p2.show)
        b3 = tk.Button(buttonframe, text="Speech to Text",  font=f,padx=10, pady=10 ,command=p3.show)

        b2.pack(side="left",fill='x')
        b3.pack(side="right",fill='x') 

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("300x300")
    root.mainloop()