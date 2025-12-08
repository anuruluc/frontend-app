import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import webbrowser
import requests

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Frontend App")
        self.geometry("800x600")

        self.navbar = ttk.Notebook(self)
        self.navbar.pack(fill="both", expand=True)

        self.notebook1 = ttk.Frame(self.navbar)
        self.navbar.add(self.notebook1, text="Home")

        self.notebook2 = ttk.Frame(self.navbar)
        self.navbar.add(self.notebook2, text="Settings")
        self.navbar.add_command(label="Open URL", command=self.open_url)

        self.label = tk.Label(self.notebook1, text="Welcome to Frontend App")
        self.label.pack(pady=100)

        self.button = tk.Button(self.notebook1, text="Click me", command=self.button_click)
        self.button.pack(pady=20)

        self.file_path = tk.StringVar()
        self.entry = tk.Entry(self.notebook2, textvariable=self.file_path)
        self.entry.pack(pady=10)

        self.open_button = tk.Button(self.notebook2, text="Open File", command=self.open_file)
        self.open_button.pack(pady=10)

        self.open_button2 = tk.Button(self.notebook2, text="Open URL", command=self.open_url)
        self.open_button2.pack(pady=10)

    def button_click(self):
        print("Button clicked")

    def open_file(self):
        file_path = filedialog.askopenfilename()
        self.file_path.set(file_path)
        print(file_path)

    def open_url(self):
        url = self.entry.get()
        webbrowser.open(url)
        print(url)

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()