import tkinter as tk
from tkinter import StringVar, Text
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

texto_recognized = []
texto = ''

class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_transcription(self, transcript):
        print(transcript)

    def on_connected(self):
        print('Connection was successful')

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))

    def on_listening(self):
        print('Service is listening')

    def on_hypothesis(self, hypothesis):
        print(hypothesis)

    def on_data(self, data):
        print(data)
        texto_recognized.append(data['results'][0]['alternatives'][0]['transcript'])

    def on_close(self):
        print("Connection closed")

# this function will initiate the recognize service and pass in the AudioSource
def recognize_using_weboscket(*args):
  mycallback = MyRecognizeCallback()
  speech_to_text.recognize_using_websocket(audio=audio_source,
                                            content_type='audio/l16; rate=44100',
                                            recognize_callback=mycallback,
                                            model='pt-BR_BroadbandModel',
                                            interim_results=True)

###############################################
#### Prepare the for recording using Pyaudio ##
###############################################

# Variables for recording the speech
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# define callback for pyaudio to store the recording in queue
def pyaudio_callback(in_data, frame_count, time_info, status):
    try:
        q.put(in_data)
    except Full:
        pass # discard
    return (None, pyaudio.paContinue)

# instantiate pyaudio
audio = pyaudio.PyAudio()
# open stream using callback
stream = audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK,
    stream_callback=pyaudio_callback,
    start=False
)

recognize_thread = Thread(target=recognize_using_weboscket, args=())
def gravar():
  #########################################################################
  #### Start the recording and start service to recognize the stream ######
  #########################################################################
  stream.start_stream()
  recognize_thread.start()
def pararGravacao():
    stream.stop_stream()
    # stream.close()
    audio.terminate()
    audio_source.completed_recording()
    texto = " ".join(str(x) for x in texto_recognized)
    print(f' o texto reconhecido>>>>>> {texto} >>>>>>')
    novo.set(texto)



ws = tk.Tk()
ws.geometry('400x300')
ws.title('Speech to text')
ws['bg']='#ffd49d'

textRecognized = tk.StringVar()
f = ("Times bold", 14)
novo = tk.StringVar()
novo.set("")

def prevPage():
    ws.destroy()
    import __main__


texto_novo = tk.Label(ws, textvariable=novo,font=f, height=10, width=40,background="#FFFFFF").pack(expand=True, fill="x")

buttonframe = tk.Frame(ws)
buttonframe.pack(side="top")


bgravar = tk.Button(buttonframe, text="Iniciar Gravação", font=f,command= gravar)
bgravar.pack(side="left", fill='x')

bparar = tk.Button(buttonframe, text="Parar Gravação", font=f, command= pararGravacao)
bparar.pack(side="left", fill='x')



buttonframe1 = tk.Frame(ws)
buttonframe1.pack(side="bottom")
b1 = tk.Button(buttonframe1, text="Inicio", font=f, command=prevPage).pack(
    fill="x", expand=True, side="left")
ws.mainloop()