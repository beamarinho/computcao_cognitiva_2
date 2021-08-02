import tkinter as tk
from .Page import Page
import pyaudio
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from threading import Thread
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

try:
    from Queue import Queue, Full
except ImportError:
    from queue import Queue, Full
###############################################
#### Initalize queue to store the recordings ##
###############################################
CHUNK = 1024
# Note: It will discard if the websocket client can't consumme fast enough
# So, increase the max size as per your choice
BUF_MAX_SIZE = CHUNK * 10
# Buffer to store audio
q = Queue(maxsize=int(round(BUF_MAX_SIZE / CHUNK)))

# Create an instance of AudioSource
audio_source = AudioSource(q, True, True)

# initialize speech to text service
authenticator = IAMAuthenticator('v_cHDfc_ZfCoZkLL8CXiWajXK9sv3h_ReT6aihbC52bV')
speech_to_text = SpeechToTextV1(authenticator=authenticator)

class SpeechToTxt(Page):
  def __init__(self, *args, **kwargs):
    Page.__init__(self,*args, **kwargs)
    f = ("Times bold", 12)
    # label = tk.Label(self, text="Speech to Text ... oi")
    # label.pack(side="top", fill="both", expand= True)

    buttonframe = tk.Frame(self)
    buttonframe.place(y=10, x=160)
    b = tk.Button(buttonframe, text="Gravar", font=f,
                  padx=10, pady=10)

    b.pack(side="right", fill='x')
