import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage


class PomodoroTimer:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title("Pomodoro, Timer Francisco")
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file="tomato.png"))

        self.root.mainloop()


PomodoroTimer()


