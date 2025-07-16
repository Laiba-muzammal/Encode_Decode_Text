# ===== utils.py =====
import string
import random

def generate_char(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))
