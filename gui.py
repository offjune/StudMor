import customtkinter as ctk
from functions import download_audio, transcribe_audio

def on_transcribe_button_click():
    url = url_entry.get()
    if not url.strip():
        result_textbox.delete("0.0", "end")
        result_textbox.insert("0.0", "Por favor, insira uma URL do YouTube.")
        return
    try:
        result_textbox.delete("0.0", "end")
        result_textbox.insert("0.0", "Baixando áudio...")
        app.update()

        arquivo_audio, titulo = download_audio(url)

        result_textbox.delete("0.0", "end")
        result_textbox.insert("0.0", "Convertendo e transcrevendo áudio, aguarde...")
        app.update()

        texto = transcribe_audio(arquivo_audio, titulo)

        result_textbox.delete("0.0", "end")
        result_textbox.insert("0.0", texto + "\n\n✅ Transcrição salva na pasta 'transcricoes'")
    except Exception as e:
        result_textbox.delete("0.0", "end")
        result_textbox.insert("0.0", f"Erro: {e}")

def create_app():
    ctk.set_appearance_mode("dark")
    global app, url_entry, result_textbox

    app = ctk.CTk()
    app.title("MorStud - Transcrição de Áudio YouTube")
    app.geometry("600x500")

    ctk.CTkLabel(app, text="Cole a URL do YouTube:").pack(pady=10)
    url_entry = ctk.CTkEntry(app, width=550)
    url_entry.pack(pady=5)

    transcribe_button = ctk.CTkButton(app, text="Iniciar Transcrição", command=on_transcribe_button_click)
    transcribe_button.pack(pady=15)

    result_textbox = ctk.CTkTextbox(app, width=580, height=300)
    result_textbox.pack(pady=10)

    return app
