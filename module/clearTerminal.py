import os
import platform

def clear_terminal():
    """
    Membersihkan layar terminal.
    Bekerja di Windows, Linux, dan macOS.
    """
    sistem_operasi = platform.system()

    if sistem_operasi == "Windows":
        os.system('cls') # Perintah untuk membersihkan terminal di Windows
    else: # Untuk Linux dan macOS
        os.system('clear') # Perintah untuk membersihkan terminal di Linux/macOS