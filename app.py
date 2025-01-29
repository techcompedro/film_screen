import tkinter as tk
import customtkinter as ctk
from film_screen import iniciar_gravacao

# Função chamada ao clicar no botão para iniciar a gravação
def iniciar_gravacao_interface():
    iniciar_gravacao()
    mostrar_mensagem("Gravação iniciada!", "green")


# Função para exibir mensagens dinâmicas na interface
def mostrar_mensagem(texto, cor="green"):
    mensagem_label.configure(text=texto, text_color=cor)

# Configuração inicial da interface
root = ctk.CTk()
root.title("Film Screen")
root.geometry("350x200")

# Definir tema para o customtkinter
ctk.set_appearance_mode("dark")  # Modo claro ou escuro
ctk.set_default_color_theme("blue")  # Tema padrão

# Estilização e layout da interface
titulo = ctk.CTkLabel(root, text="FILM SCREEN", font=("Arial", 20, "bold"))
titulo.pack(pady=10)

frame = ctk.CTkFrame(root)
frame.pack(padx=20, pady=20, fill="both", expand=True)

botao_iniciar = ctk.CTkButton(frame, text="Iniciar Gravação", command=iniciar_gravacao_interface, width=200)
botao_iniciar.pack(pady=10)



instrucoes_label = ctk.CTkLabel(
    frame, 
    text="A gravação será encerrada ao pressionar as teclas Alt + P.",
    wraplength=300,
    justify="center"
)
instrucoes_label.pack(pady=10)

mensagem_label = ctk.CTkLabel(frame, text="", font=("Arial", 14))
mensagem_label.pack(pady=10)

root.mainloop()
