import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox 
import fitz
from PIL import Image
import os
from pathlib import Path

def choose_folder():
    folder_path = filedialog.askdirectory()
    return folder_path

def pdf_to_jpg(folder_path):
    for pdf_file in os.listdir(folder_path):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, pdf_file)
            pdf_document = fitz.open(pdf_path)
            for page_number in range(pdf_document.page_count):
                page = pdf_document.load_page(page_number)
                image = page.get_pixmap()
                file_name = Path(pdf_file).stem
                image.save(f'{file_name}.jpg')

# Создание окна
root = tk.Tk()
root.title("PDF в JPG")

# Функция обработки нажатия на кнопку выбора папки
def select_folder():
    folder_path = choose_folder()
    print(f"Выбрана папка: {folder_path}")

# Функция обработки нажатия на кнопку конвертации PDF в JPG
def convert_to_jpg():
    folder_path = choose_folder()
    print(f"Конвертация PDF файлов в JPG в папке: {folder_path}")
    pdf_to_jpg(folder_path)
    print("Конвертация завершена.")
    messagebox.showinfo('Перевод PDF в JPG', 'Готово.\n Конвертация завершена!')

root.configure(background='gray')
convert_to_jpg_button = tk.Button(root, text="Конвертировать PDF в JPG", command=convert_to_jpg, padx=25, pady=25).grid(row=0, column=0,padx=30, pady=30)
root.mainloop()

