import os
import subprocess
from pytubefix import YouTube
from pytubefix.cli import on_progress
import whisper
import re

model = whisper.load_model("base")

def limpar_nome_arquivo(nome):

    return re.sub(r'[\\/*?:"<>|]', "", nome)

def download_audio(url, output_dir="audios"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    yt = YouTube(url, on_progress_callback=on_progress)
    audio_stream = yt.streams.get_audio_only()
    arquivo_audio = audio_stream.download(output_path=output_dir)
    return arquivo_audio, yt.title

def converter_para_wav(input_file, output_file="temp.wav"):
    command = [
        "ffmpeg",
        "-y",
        "-i", input_file,
        "-ac", "1",
        "-ar", "16000",
        output_file
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return output_file

def transcribe_audio(arquivo_audio, titulo, idioma="pt", pasta_transcricoes="transcricoes"):
    if not os.path.exists(pasta_transcricoes):
        os.makedirs(pasta_transcricoes)

    arquivo_wav = converter_para_wav(arquivo_audio)
    result = model.transcribe(arquivo_wav, language=idioma, beam_size=1)
    texto = result["text"]


    nome_limpo = limpar_nome_arquivo(titulo)
    caminho_txt = os.path.join(pasta_transcricoes, f"{nome_limpo}.txt")
    with open(caminho_txt, "w", encoding="utf-8") as f:
        f.write(texto)


    try:
        if os.path.exists(arquivo_audio):
            os.remove(arquivo_audio)
        if os.path.exists(arquivo_wav):
            os.remove(arquivo_wav)
    except Exception as e:
        print(f"Erro ao apagar arquivos de áudio: {e}")

    return texto
