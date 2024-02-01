from tkinter import *
from tkinter import ttk
import cv2
from PIL import Image, ImageTk

img = cv2.VideoCapture(0)
img.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
img.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

wnd = Tk()
wnd.title("Camera")
wnd_x_size = 800
wnd_y_size = 600
screen_x_size = wnd.winfo_screenwidth()
screen_y_size = wnd.winfo_screenheight()
center_x = int((screen_x_size - wnd_x_size) / 2)
center_y = int((screen_y_size - wnd_y_size) / 2)
wnd.geometry(f'{wnd_x_size}x{wnd_y_size}+{center_x}+{center_y}')
wnd.resizable(False, False)

wnd.bind('<Escape>', lambda q: wnd.quit())

label_cam = Label(wnd)
label_cam.pack()

def open_cam():
    _, frame = img.read()
    cv2_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    cap_image = Image.fromarray(cv2_frame)
    photo_image = ImageTk.PhotoImage(image=cap_image)
    label_cam.photo_image = photo_image
    label_cam.configure(image=photo_image)
    label_cam.after(50, open_cam)

def screenshot():
    _, frame = img.read()
    cv2_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    cap_image = Image.fromarray(cv2_frame)
    cap_image.save("screenshot.png")

# Stworzenie ramki na przyciski
button_frame = Frame(wnd)
button_frame.pack(side="bottom", pady=10)

button_cam = ttk.Button(button_frame, text="Camera", command=open_cam)
button_cam.pack(side="left", padx=10)

screenshot_btn = ttk.Button(button_frame, text="Screenshot", command=screenshot)
screenshot_btn.pack(side="right", padx=10)

wnd.mainloop()
