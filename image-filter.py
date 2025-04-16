import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

#Creating the GUI window
root = tk.Tk()
root.title("Image Filter App")
root.geometry("600x500")

img = None
panel = None

def open_image():
    global img, panel
    filepath = filedialog.askopenfilename()
    if filepath:
        img = cv2.imread(filepath)
        show_image(img)

def show_image(cv_img):
    global panel
    rgb_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb_img)
    pil_img = pil_img.resize((400, 300))
    tk_image = ImageTk.PhotoImage(pil_img)

    if panel is None:
        panel = tk.Label(image=tk_image)
        panel.image = tk_image
        panel.pack(pady=20)
    else:
        panel.configure(image=tk_image)
        panel.image = tk_image

def apply_grayscale():
    if img is not None:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        show_image(cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR))

def apply_blur():
    if img is not None:
        blur = cv2.GaussianBlur(img, (15, 15), 0)
        show_image(blur)

def apply_edge():
    if img is not None:
        edge = cv2.Canny(img, 100, 200)
        show_image(cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR))

def save_image():
    if img is not None:
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        if file_path:
            cv2.imwrite(file_path, img)
            print("Image saved!")


tk.Button(root, text="Open Image", command=open_image).pack(pady=5)
tk.Button(root, text="Grayscale", command=apply_grayscale).pack(pady=5)
tk.Button(root, text="Blur", command=apply_blur).pack(pady=5)
tk.Button(root, text="Edge Detection", command=apply_edge).pack(pady=5)
tk.Button(root, text="Save Image", command=save_image).pack(pady=5)

root.mainloop()
