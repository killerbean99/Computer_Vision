import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def extract_text_from_image(file_path=None, language = 'eng'):
    root = tk.Tk()
    root.withdraw()  # Скрыть главное окно

    if not file_path:
        file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=(("Image files", "*.png;*.jpg;*.jpeg;*.bmp"), ("All files", "*.*"))
    )

    if file_path:  # Проверка: вдруг пользователь отменил выбор
        text = pytesseract.image_to_string(Image.open(file_path), lang=language)
        print(text)
        return text
    else:
        print("Файл не выбран.")
        return None
