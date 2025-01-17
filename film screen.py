import cv2
import numpy as np
import pyautogui
import pyaudio
import wave
import threading
import keyboard
from moviepy import VideoFileClip, AudioFileClip

# Configurações de áudio
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
audio_frames = []

# Função para gravar áudio
def gravar_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    
    while not stop_recording.is_set():
        data = stream.read(CHUNK)
        audio_frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

# Inicia a gravação de áudio em uma thread separada
stop_recording = threading.Event()
thread = threading.Thread(target=gravar_audio)
thread.start()

# Configurações de vídeo
fps = 20.0
largura, altura = pyautogui.size()
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter("gravacao_temp.mp4", fourcc, fps, (largura, altura))

print("Pressione 'q' para parar a gravação.")

# Gravação da tela
while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    video.write(frame)

    if keyboard.is_pressed('q'):
        print("Gravação parada.")
        break

# Finaliza a gravação
stop_recording.set()
thread.join()
video.release()

# Salva o áudio gravado
audio_file = "gravacao_audio.wav"
with wave.open(audio_file, "wb") as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pyaudio.PyAudio().get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(audio_frames))

# Combina o vídeo e o áudio
video_clip = VideoFileClip("gravacao_temp.mp4")
audio_clip = AudioFileClip(audio_file)

# Define o áudio do vídeo
final_clip = video_clip.with_audio(audio_clip)

# Salva o vídeo final
final_clip.write_videofile("gravacao_final.mp4", codec="libx264")

# Limpeza
video_clip.close()
audio_clip.close()
final_clip.close()

# Remove arquivos temporários
import os
os.remove("gravacao_temp.mp4")
os.remove(audio_file)

print("Gravação finalizada e combinada em 'gravacao_final.mp4'.")