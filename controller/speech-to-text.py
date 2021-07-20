import pyaudio
import wave

# filename -> .wav
def read_audio(filename):
  # quantidade de amostras por data frame
  chunk = 1024

  # abrir o arquivo de audio
  wf = wave.open(filename, 'rb')

  # interface do PortAudio
  p = pyaudio.PyAudio()

  # Abri um objeto .Stream para escrever o arquivo WAV para
  # output = True indica que o som será reproduzido ao invéz de gravado
  stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                  channels = wf.getnchannels(),
                  rate = wf.getframerate(),
                  output = True) 

  data = wf.readframes(chunk)

  # Play!  escreve o audio para stream
  while data != '':
      stream.write(data)
      data = wf.readframes(chunk)

  # Close and terminate the stream
  stream.close()
  p.terminate()

# def speech_to_text(filename)