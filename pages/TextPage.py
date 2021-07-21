import tkinter as tk
from .Page import Page
class TxtToSpeech(Page):
    f = ("Times bold", 12) 

    def __init__(self, *args, **kwargs):
        Page.__init__(self,*args, **kwargs)
        label = tk.Label(self, text="Text to Speech")
        label.pack(side="top", fill="x", expand= True)

        text = tk.Text(self, background="#FFFFFF",height=100,width=250)
        text.pack()