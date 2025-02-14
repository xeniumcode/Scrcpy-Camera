import tkinter as tk
from v4l2loopback import create_virtcam
from app import ScrcpyApp

# Define the video device number
VIDEO_NR = 5

if __name__ == "__main__":
    if create_virtcam(VIDEO_NR):
        root = tk.Tk()
        app = ScrcpyApp(root)
        root.mainloop()
    else:
        print(f"Failed to set up virtual camera (video{VIDEO_NR}). Exiting.")
