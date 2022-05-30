import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage


class PomodoroTimer:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title("Pomodoro, Timer Francisco")
        # TODO: Image not loading. .jpg files are not loaded by default in tkinter
        #       you need to use PIL --> https://stackoverflow.com/a/48492788/1866109
        # self.root.iconphoto(False, PhotoImage(file="Baeldung.png"))
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file="tomato.png"))

        self.root.mainloop()


PomodoroTimer()


