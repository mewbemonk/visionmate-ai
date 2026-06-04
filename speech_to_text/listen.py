import whisper
import sounddevice as sd




model  = whisper.load_model("base")
samplerate = 16000

def listen():

    print("listening...")
    
    audio = sd.rec(samplerate*5, samplerate=samplerate, channels=1, dtype='float32')

    sd.wait()

    mic = audio.flatten()

    res = model.transcribe(
        mic,
       
    )


    return res['text'].strip()



print(listen())