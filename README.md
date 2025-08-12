<h1 align="center" style="color:#f5f5f5;background-color:#0d1117;padding:10px;border-radius:8px;">🎙️ MorStud - Transcrição de Áudio do YouTube</h1>

<p align="center">
  Aplicação em Python com interface gráfica usando <strong>CustomTkinter</strong> para baixar, converter e transcrever áudio de vídeos do YouTube com <strong>Whisper</strong>.
</p>

---

## ✨ Funcionalidades

- 🎧 Baixa áudio do YouTube via pytubefix  
- 🔄 Converte áudio para WAV usando FFmpeg (mono, 16kHz)  
- 📝 Transcreve o áudio com Whisper (modelo base)  
- 💾 Salva transcrição em arquivo texto com nome do vídeo  
- 🗑 Remove arquivos de áudio temporários automaticamente  
- 🖥 Interface gráfica simples e intuitiva

---

## 🛠 Tecnologias Utilizadas

<div align="center" style="background-color:#0d1117;padding:10px;border-radius:8px;">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="Python"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/ffmpeg/ffmpeg-original.svg" height="40" alt="FFmpeg"/>
  <img src="https://github.com/TomSchimansky/CustomTkinter/raw/main/docs/source/_static/customtkinter-logo.png" height="40" alt="CustomTkinter"/>
</div>

---

## 📂 Estrutura do Projeto

```
📦 MorStud
 ┣ 📜 app.py               # Script principal que inicia a GUI
 ┣ 📜 gui.py               # Interface gráfica com CustomTkinter
 ┣ 📜 functions.py         # Funções de download, conversão e transcrição
 ┣ 📂 audios               # Áudios baixados temporariamente
 ┣ 📂 transcricoes         # Transcrições salvas em arquivos .txt
 ┣ 📜 requirements.txt     # Dependências Python
 ┗ 📜 README.md            # Documentação do projeto
```
## 🎯 Como Usar

Clone o repositório:
```
git clone https://github.com/seuusuario/morstud.git
cd morstud
```
Crie e ative ambiente virtual (opcional):
```
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```
Instale as dependências:
```
pip install -r requirements.txt
```
Instale o FFmpeg e adicione ao PATH do sistema:
https://ffmpeg.org/download.html

Execute o programa:

```
python app.py
```
Na janela que abrir:

Cole a URL do vídeo do YouTube

Clique em Iniciar Transcrição

Aguarde o processamento

Veja o texto na área de resultados

Transcrição salva em transcricoes/

Áudios temporários removidos automaticamente

##📜 Licença

Projeto sob licença MIT. Use, modifique e compartilhe livremente.

Desenvolvido por June com ❤️
