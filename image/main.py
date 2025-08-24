import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO

window = tk.Tk()
window.title("Генератор лис")
window.geometry("500x550")

title_label = tk.Label(window, text="Нажми кнопку для новой лисы!", font=("Arial", 14))
title_label.pack(pady=10)

image_label = tk.Label(window)
image_label.pack(pady=10)


def get_fox():
    try:
        fox_data = requests.get("https://randomfox.ca/floof/").json()
        fox_url = fox_data['image']

        img_response = requests.get(fox_url)
        img_data = Image.open(BytesIO(img_response.content))

        img_data.thumbnail((400, 400))

        fox_photo = ImageTk.PhotoImage(img_data)

        image_label.config(image=fox_photo)
        image_label.image = fox_photo

    except:
        error_text = "Ошибка загрузки"
        image_label.config(text=error_text)


fox_button = tk.Button(window, text="Новая лиса!", command=get_fox, font=("Arial", 12))
fox_button.pack(pady=10)

get_fox()

window.mainloop()