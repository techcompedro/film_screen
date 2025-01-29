import cv2
import numpy as np
import pyautogui
import pyaudio
import wave
import threading
import keyboard
import os
from moviepy import VideoFileClip, AudioFileClip
import customtkinter as ctk
import datetime
# Configurações de áudio
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
audio_frames = []

# Função para verificar se há microfone disponível
def verificar_microfone():
    audio = pyaudio.PyAudio()
    for i in range(audio.get_device_count()):
        device_info = audio.get_device_info_by_index(i)
        if device_info['maxInputChannels'] > 0:
            print("Microfone encontrado!")
            return True
    print("Nenhum microfone encontrado. Verifique a conexão.")
    return False

# Função para gravar áudio
def gravar_audio(stop_recording):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    
    while not stop_recording.is_set():
        data = stream.read(CHUNK)
        audio_frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

# Função para gravar a tela
def gravar_tela(stop_recording):
    fps = 20.0
    largura, altura = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video = cv2.VideoWriter("gravacao_temp.mp4", fourcc, fps, (largura, altura))
    
    while not stop_recording.is_set():
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video.write(frame)
    
    video.release()

# Função que será chamada ao pressionar o botão
def iniciar_gravacao():
    # Verifica se há microfone disponível
    if verificar_microfone():
        stop_recording = threading.Event()

        # Inicia a gravação de áudio e vídeo em threads separadas
        audio_thread = threading.Thread(target=gravar_audio, args=(stop_recording,))
        video_thread = threading.Thread(target=gravar_tela, args=(stop_recording,))

        audio_thread.start()
        video_thread.start()

        # Aguarda o término da gravação ao pressionar 'Alt + P'
        while True:
            if keyboard.is_pressed('alt+p'):
                print("Gravação parada.")
                break

        # Para a gravação
        stop_recording.set()
        audio_thread.join()
        video_thread.join()

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
        time_now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        # Salva o vídeo final
        final_clip.write_videofile(f"gravacao_{time_now}.mp4", codec="libx264")

        # Limpeza
        video_clip.close()
        audio_clip.close()
        final_clip.close()

        # Remove arquivos temporários
        os.remove("gravacao_temp.mp4")
        os.remove(audio_file)

        print("Gravação finalizada e combinada em 'gravacao_final.mp4'.")
    else:
        print("Não é possível continuar sem microfone.")

# Criação da interface
def interface_basica():
    app = ctk.CTk()
    app.title("Gravação de Tela e Áudio")
    
    # Botão de iniciar gravação
    button = ctk.CTkButton(app, text="Iniciar Gravação", command=iniciar_gravacao)
    button.pack(padx=20, pady=70)
    app.geometry("200x190")
    # Execução da interface
    app.mainloop()



