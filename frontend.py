from tkinter import ttk
import sv_ttk
import subprocess
import time

class ScrcpyApp:
    def __init__(self,master):
        self.master = master
        master.title("Scrcpy WebCam Controller")
        master.geometry("560x390")
        master.protocol("WM_DELETE_WINDOW", self.on_close)

        sv_ttk.set_theme("dark")

        self.create_window()
        self.process = None

    def create_window(self):
        main_frame = ttk.Frame(self.master)
        main_frame.pack(expand=True, fill='both')

        status_frame = ttk.Frame(main_frame)
        status_frame.pack(side='top', fill='x', padx=10, pady=10)
        self.status_label = ttk.Label(status_frame, text="Status: Idle", font=("Arial", 12))
        self.status_label.pack(side='left')

        button_frame = ttk.Frame(main_frame)
        button_frame.pack(side='bottom', fill='both', expand=True)
        button_frame.columnconfigure((0, 1), weight=1)
        button_frame.rowconfigure((0, 1), weight=1)
        self.front_camera_btn = ttk.Button(button_frame, text="Front Camera", command=self.front_camera,style="Camera.TButton")
        self.back_camera_btn = ttk.Button(button_frame, text="Back Camera", command=self.back_camera,style="Camera.TButton")
        self.stop_btn = ttk.Button(button_frame, text="Stop", command=self.stop_camera,style="Camera.TButton")
        style = ttk.Style()
        style.configure("Camera.TButton", font=("Arial", 18, "bold"))
        self.front_camera_btn.grid(row=0, column=0, sticky='nsew', padx=3, pady=3)
        self.back_camera_btn.grid(row=0, column=1, sticky='nsew', padx=3, pady=3)
        self.stop_btn.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=3, pady=3)

    def run_scrcpy(self, camera):
        command = [
            "scrcpy",
            "--video-source=camera",
            "--no-audio",
            f"--camera-facing={camera}",
            "--v4l2-sink=/dev/video5",
            "--max-size=800"
        ]
        self.stop_camera()  # Stop any existing process
        self.process = subprocess.Popen(command)
        self.current_camera = camera
        self.update_status(f"{camera.capitalize()} Camera Active")

    def front_camera(self):
        print("Front Camera activated")
        self.run_scrcpy("front")

    def back_camera(self):
        print("Back Camera activated")
        self.run_scrcpy("back")

    def stop_camera(self):
        print("Camera stopped")
        if self.process:
            self.process.kill()
            self.process = None
        self.current_camera = None
        self.update_status("Idle")

    def update_status(self, status):
        self.status_label.config(text=f"Status: {status}")

    def on_close(self):
        self.update_status("Closing...")
        self.stop_camera()
        time.sleep(0.5)
        self.master.destroy()
