# app.py

import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Meal Planner and Grocery System")
        self.root.geometry("800x600")

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
