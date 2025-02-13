import tkinter as tk 
from tkinter import ttk
import sv_ttk

class ScrcpyApp:
    def __init__(self,master):
        self.master = master
        master.title("Scrcpy WebCam Controller")
        master.geometry("560x390")

        # Apply Sun Valley Theme
        sv_ttk.set_theme("dark")

        self.create_window()

    def create_window(self):
        # Main Frame
        main_frame = ttk.Frame(self.master)
        main_frame.pack(expand=True, fill='both')

        # Button Frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(side='bottom', fill='both', expand=True)

        # Setting up the button's Row and Column
        button_frame.columnconfigure((0, 1), weight=1)
        button_frame.rowconfigure((0, 1), weight=1)

        # Creating the Buttons
        self.front_camera_btn = ttk.Button(button_frame, text="Front Camera", command=self.front_camera,style="Camera.TButton")
        self.back_camera_btn = ttk.Button(button_frame, text="Back Camera", command=self.back_camera,style="Camera.TButton")
        self.stop_btn = ttk.Button(button_frame, text="Stop", command=self.stop_camera,style="Camera.TButton")

        # Configuring the style for the Camera Button
        style = ttk.Style()
        style.configure("Camera.TButton", font=("Arial", 18, "bold"))

        # Placing the Buttons
        self.front_camera_btn.grid(row=0, column=0, sticky='nsew', padx=3, pady=3)
        self.back_camera_btn.grid(row=0, column=1, sticky='nsew', padx=3, pady=3)
        self.stop_btn.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=3, pady=3)

    # Logic for the Buttons
    def front_camera(self):
        print("Front Camera activated")

    def back_camera(self):
        print("Back Camera activated")

    def stop_camera(self):
        print("Camera stopped")

if __name__ == "__main__":
    root = tk.Tk()
    ScrcpyApp(root)
    root.mainloop()