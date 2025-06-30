# Caesar_cipher
A simple Python implementation of Caesar Cipher that supports both encoding and decoding text with a custom shift value. Built as a beginner-friendly terminal application
# Caesar Cipher - Python

This is a basic Python implementation of the classic **Caesar Cipher** encryption algorithm.

The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

---

## 🚀 Features

- 🔒 Encode (encrypt) messages
- 🔓 Decode (decrypt) messages
- 🔁 Loop interface – continue encoding/decoding until "stop" is typed
- 🔡 Works with lowercase text
- ✅ Handles shift values ​​beyond 26 by modulo operation

---

## ▶️ How to Run

> Requires: Python Python 3.7.9 or higher

Clone the repository and run the script:

```bash
python caesar_cipher.py

Type 'encode' to encrypt, 'decode' to decrypt, or 'stop' to exit:
encode
Type your message:
hello
Type the shift number:
4
The encoded text is: lipps

caesar_cipher/
├── caesar_cipher.py
└── README.md
└── logo.py
└── alphabet.py
====================================================================================================================
🎓 Educational Purpose
This project was developed for learning purposes as part of Python programming practice. You can expand it to support:

Uppercase characters

Non-alphabet characters

File input/output

GUI interface with Tkinter or PyQt

