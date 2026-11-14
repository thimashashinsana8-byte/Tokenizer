import unicodedata

def normalize_text(text):
    normalized = unicodedata.normalize("NFC", text)
    return normalized
