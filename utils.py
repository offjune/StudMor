import re

def validar_url_youtube(url: str) -> bool:
    regex = r"(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+"
    return re.match(regex, url) is not None
