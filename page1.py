import tkinter as tk
from os import O_TEMPORARY, read
from ibm_watson import TextToSpeechV1
from ibm_watson.websocket import SynthesizeCallback
import pyaudio
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from functools import partial

authenticator = IAMAuthenticator(
    'mjmwxDNMSQ0E1lh0Ucivl5yRdI3471IZniPqJ2qVaAD9')
service = TextToSpeechV1(authenticator=authenticator)





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

ws = tk.Tk()
ws.geometry('400x300')
ws.title('Text to speech')
ws['bg'] = '#ffbf00'

f = ("Times bold", 14)


def prevPage():
    ws.destroy()
    import __main__

  
test_callback = MySynthesizeCallback()

def lerTexto():
  texto = text.get("1.0", "end-1c")
  service.synthesize_using_websocket(texto,
                                      test_callback,
                                      accept='audio/wav',
                                      voice="pt-BR_IsabelaVoice"
                                      )
  print(texto)

label = tk.Label(ws, text="Text to Speech", font=f, bg='#ffbf00')
label.pack(side="top")

buttonframe1 = tk.Frame(ws)
buttonframe1.pack(side="bottom")



b1 = tk.Button(buttonframe1, text="Inicio", font=f,padx=10, pady=10, command=prevPage).pack(
    fill="x", expand=True, side="left")

text = tk.Text(ws, background="#FFFFFF", height=10, width=40)
text.pack()

texto = text.get("1.0", "end-1c")

buttonframe2 = tk.Frame(ws)
buttonframe2.pack(side="bottom")
b = tk.Button(buttonframe2, text="Ler o texto", font=f, command= lambda: lerTexto())
    
b.pack(side="right", fill='x')
ws.mainloop()