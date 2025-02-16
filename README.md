# Film Screen

## Descrição Geral
O **Film Screen** é uma aplicação desenvolvida em Python que permite a gravação simultânea de áudio e vídeo da tela do computador. Utiliza bibliotecas como `cv2`, `pyautogui`, `pyaudio`, `moviepy` e `customtkinter` para fornecer uma interface gráfica intuitiva e funcionalidades robustas de gravação.

## Componentes Principais
- **Interface Gráfica**: Desenvolvida com `customtkinter`, oferece uma interface amigável para iniciar e gerenciar gravações.
- **Gravação de Áudio**: Utiliza `pyaudio` para capturar áudio do microfone.
- **Gravação de Vídeo**: Utiliza `pyautogui` para capturar a tela e `cv2` para processar e salvar o vídeo.
- **Combinação de Áudio e Vídeo**: Utiliza `moviepy` para unir os arquivos de áudio e vídeo em um único arquivo final.

## Funcionamento do Sistema
### 1. Inicialização
- O sistema inicia com a configuração da interface gráfica, onde o usuário pode clicar em um botão para iniciar a gravação.

### 2. Verificação de Microfone
- Antes de iniciar a gravação, o sistema verifica se um microfone está disponível. Se não houver microfone, a gravação não pode prosseguir.

### 3. Gravação
- Ao clicar no botão **"Iniciar Gravação"**, duas threads são iniciadas:
  - **Thread de Áudio**: Captura o áudio do microfone em tempo real.
  - **Thread de Vídeo**: Captura a tela do computador em tempo real.
- A gravação continua até que o usuário pressione a combinação de teclas **`Alt + P`**, que sinaliza o término da gravação.

### 4. Finalização
- Após a gravação ser interrompida:
  - Os dados de áudio e vídeo são salvos em arquivos temporários.
  - O sistema combina o áudio e o vídeo em um único arquivo usando `moviepy`.
  - O arquivo final é salvo com um timestamp no nome, e os arquivos temporários são removidos automaticamente.

## Funcionalidades Adicionais
- **Mensagens Dinâmicas**: O sistema exibe mensagens na interface para informar o usuário sobre o status da gravação (exemplo: "Gravação iniciada!" ou "Gravação finalizada.").
- **Instruções**: O sistema fornece instruções sobre como iniciar e encerrar a gravação de forma simples e eficiente.

## Conclusão
O **Film Screen** é uma ferramenta eficaz para gravação de tela e áudio, com uma interface intuitiva e funcionalidades robustas. É ideal para criação de tutoriais, gravação de apresentações ou captura de qualquer atividade na tela do computador.

---

### Requisitos
Para utilizar o **Film Screen**, certifique-se de ter as seguintes bibliotecas instaladas:
```bash
pip install opencv-python pyautogui pyaudio moviepy customtkinter
```

### Execução
Para executar a aplicação, basta rodar o seguinte comando:
```bash
python app.py
```

