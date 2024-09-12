import sounddevice
from scipy.io.wavfile import write
fs=44100
second=int(input("Enter The Time Duration In Seond        "))
print("RECORDING...")
record=sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
sounddevice.wait()
write("out.wav",fs,record)
print("Finished")
