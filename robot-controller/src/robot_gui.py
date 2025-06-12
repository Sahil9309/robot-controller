import os
import tkinter as tk
from controller import RobotController
from PIL import Image, ImageTk
import requests
from io import BytesIO

COORD_FILE = "/tmp/coordinates.txt"
FRAME_FILE = "/tmp/last_frame.jpg"

# Replace with your phone's IP and port
FRAME_URL = "http://192.168.182.63:8080/shot.jpg"  # <-- Change this to your actual IP:port

def save_coordinates(x, y):
    with open(COORD_FILE, "w") as f:
        f.write(f"{x},{y}")

class RobotGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Robot Controller")
        self.controller = RobotController()
        self.controller.start()

        self.coord_label = tk.Label(master, text="Coordinates: (0, 0)", font=("Arial", 16, "bold"), fg="#333")
        self.coord_label.pack(pady=10)

        btn_frame = tk.Frame(master, bg="#e0e0e0", bd=2, relief="ridge")
        btn_frame.pack(pady=10)

        btn_style = {
            "font": ("Arial", 14, "bold"),
            "bg": "#4CAF50",
            "fg": "white",
            "activebackground": "#388E3C",
            "activeforeground": "white",
            "width": 8,
            "height": 2,
            "bd": 0,
            "relief": "raised",
            "cursor": "hand2"
        }

        self.up_btn = tk.Button(btn_frame, text="▲", command=lambda: self.move(0, 1), **btn_style)
        self.up_btn.grid(row=0, column=1, padx=8, pady=8)

        self.left_btn = tk.Button(btn_frame, text="◀", command=lambda: self.move(-1, 0), **btn_style)
        self.left_btn.grid(row=1, column=0, padx=8, pady=8)

        self.down_btn = tk.Button(btn_frame, text="▼", command=lambda: self.move(0, -1), **btn_style)
        self.down_btn.grid(row=1, column=1, padx=8, pady=8)

        self.right_btn = tk.Button(btn_frame, text="▶", command=lambda: self.move(1, 0), **btn_style)
        self.right_btn.grid(row=1, column=2, padx=8, pady=8)

        # Show Webcam Button
        self.show_webcam = False
        self.webcam_button = tk.Button(master, text="Show Webcam", command=self.toggle_webcam,
                                       font=("Arial", 14, "bold"), bg="#2196F3", fg="white",
                                       activebackground="#1565C0", activeforeground="white",
                                       width=16, height=2, bd=0, relief="raised", cursor="hand2")
        self.webcam_button.pack(pady=15)

        self.webcam_label = tk.Label(master, bd=2, relief="sunken")
        self.webcam_label.pack(pady=10)

    def move(self, dx, dy):
        self.controller.update_coordinates(dx, dy)
        x, y = self.controller.get_coordinates()
        self.coord_label.config(text=f"Coordinates: ({x}, {y})")
        save_coordinates(x, y)  # Save to file

    def toggle_webcam(self):
        self.show_webcam = not self.show_webcam
        if self.show_webcam:
            self.webcam_button.config(text="Hide Webcam")
            self.update_webcam()
        else:
            self.webcam_button.config(text="Show Webcam")
            self.webcam_label.config(image='')

    def update_webcam(self):
        if self.show_webcam:
            try:
                response = requests.get(FRAME_URL, timeout=1)
                img_data = BytesIO(response.content)
                img = Image.open(img_data)
                img = img.resize((320, 240))
                self.webcam_img = ImageTk.PhotoImage(img)
                self.webcam_label.config(image=self.webcam_img)
            except Exception:
                pass
            self.master.after(200, self.update_webcam)

if __name__ == "__main__":
    # Save initial coordinates
    save_coordinates(0, 0)
    root = tk.Tk()
    app = RobotGUI(root)
    root.mainloop()