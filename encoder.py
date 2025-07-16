
# ===== encoder.py =====
from utils import generate_char

def encode(text):
    if len(text) == 1:
        return text
    elif len(text) == 2:
        return text[::-1]
    else:
        start = text[0]
        text = text[1:] + start
        random_start = generate_char(3)
        random_end = generate_char(3)
        return random_start + text + random_end
