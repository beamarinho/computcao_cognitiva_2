import tkinter as tk
from .Page import Page


class SpeechToTxt(Page):
  def __init__(self, *args, **kwargs):
      Page.__init__(self,*args, **kwargs)
      label = tk.Label(self, text="Speech to Text ... oi")
      label.pack(side="top", fill="both", expand= True)
