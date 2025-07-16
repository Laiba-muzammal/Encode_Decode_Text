
# ===== decoder.py =====
def decode(text):
    if len(text) == 1:
        return text
    elif len(text) == 2:
        return text[::-1]
    elif len(text) > 6:
        new_text = text[3:-3]
        return new_text[-1] + new_text[:-1]
    else:
        return "Improper Text!"
