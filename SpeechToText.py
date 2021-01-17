from deepspeech import Model
import numpy as np
import os
import wave

ds = Model("deepspeech-0.9.3-models.tflite")

def readWavFile(file):
    with wave.open(file, "rb") as w:
        rate = w.getframerate()
        frames = w.getnframes()
        buffer = w.readframes(frames)
    return buffer, rate

def transcribe(file):
    buffer, rate = readWavFile(file)
    data16 = np.frombuffer(buffer, dtype=np.int16)
    return ds.stt(data16)

file = open("speechOutput.txt", "w")

file.write(transcribe("4507-16021-0012.wav"))

file.close()