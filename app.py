import tkinter as tk 


class ScrcpyApp:
    def __init__(self,master):
        self.master = master
        master.title("Scrcpy WebCam Controller")
        master.geometry("560x390")
        master.configure(bg="#040406")

if __name__ == "__main__":
    root = tk.Tk()
    ScrcpyApp(root)
    root.mainloop()