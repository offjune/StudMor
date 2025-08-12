import os
import subprocess
from pytubefix import YouTube
from pytubefix.cli import on_progress
import whisper

model = whisper.load_model("base")

def download_audio(url, output_dir="audios"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    yt = YouTube(url, on_progress_callback=on_progress)
    audio_stream = yt.streams.get_audio_only()
    arquivo_audio = audio_stream.download(output_path=output_dir)
    return arquivo_audio

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

def transcribe_audio(arquivo_audio, idioma="pt"):
    arquivo_wav = converter_para_wav(arquivo_audio)
    result = model.transcribe(arquivo_wav, language=idioma, beam_size=1)
    return result["text"]
