from os import O_TEMPORARY, read
import tkinter as tk
from tkinter.constants import X
from .Page import Page
# from controller.Text2speech import Play
from functools import partial


from ibm_watson import TextToSpeechV1
from ibm_watson.websocket import SynthesizeCallback
import pyaudio
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('mjmwxDNMSQ0E1lh0Ucivl5yRdI3471IZniPqJ2qVaAD9')
service = TextToSpeechV1(authenticator=authenticator)
class TxtToSpeech(Page):
  def __init__(self, *args, **kwargs):
    Page.__init__(self, *args, **kwargs)
    f = ("Times bold", 12)
    label = tk.Label(self, text="Text to Speech")
    label.place(y=0, x=150)
    # label.pack(side="top", fill="x", expand= True)

    text = tk.Text(self, background="#FFFFFF", height=10, width=40)
    text.place(y=30, x=30)
    # text.pack(expand=False,side="top")

    texto = text.get("1.0", "end-1c")

    buttonframe = tk.Frame(self)
    buttonframe.place(y=250, x=150)
    b = tk.Button(buttonframe, text="Ler o texto", font=f,
                  padx=10, pady=10, command=lambda: lerTexto(text.get("1.0", "end-1c")))
    
    b.pack(side="right", fill='x')




class Play(object):
    """
    Wrapper to play the audio in a blocking mode
    """
    def __init__(self):
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 22050
        self.chunk = 1024
        self.pyaudio = None
        self.stream = None

    def start_streaming(self):
        self.pyaudio = pyaudio.PyAudio()
        self.stream = self._open_stream()
        self._start_stream()

    def _open_stream(self):
        stream = self.pyaudio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            output=True,
            frames_per_buffer=self.chunk,
            start=False
        )
        return stream

    def _start_stream(self):
        self.stream.start_stream()

    def write_stream(self, audio_stream):
        self.stream.write(audio_stream)

    def complete_playing(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pyaudio.terminate()

class MySynthesizeCallback(SynthesizeCallback):
    def __init__(self):
        SynthesizeCallback.__init__(self)
        self.play = Play()

    def on_connected(self):
        print('Opening stream to play')
        self.play.start_streaming()

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_timing_information(self, timing_information):
        print(timing_information)

    def on_audio_stream(self, audio_stream):
        self.play.write_stream(audio_stream)

    def on_close(self, ws, **kwargs):
        print('Completed synthesizing')
        self.play.complete_playing()


test_callback = MySynthesizeCallback()

def lerTexto(texto):
  service.synthesize_using_websocket(texto,
                                  test_callback,
                                  accept='audio/wav',
                                  voice="pt-BR_IsabelaVoice"
                                )
  print(texto)
