### 🧪 Text Encoder-Decoder
A beginner-friendly Python CLI app that lets you encode and decode text using simple logic with added obfuscation.

---

### 🚀 Features
#### 🔒 Encoding

1-character input → returned as-is

2-character input → reversed

3+ characters → rotate 1st letter to end and surround with 3 random letters on both sides

#### 🔓 Decoding

Remove first and last 3 random letters

Shift last character to front to restore original

---

### 🛠 How to Run

```bash
python main.py
```

> You’ll be prompted to enter text and choose between encoding or decoding.

---

### 🗂 Project Structure
```bash
text_encoder_decoder/
├── main.py          # Main CLI program
├── encoder.py       # Encoding logic
├── decoder.py       # Decoding logic
├── utils.py         # Random string generator
└── README.md        # Documentation
```

---

### 📌 Example
Input: hello
Encoding Output: XyZellohAqT
Decoding Output: hello

---

> (Note: The random characters will vary.)
