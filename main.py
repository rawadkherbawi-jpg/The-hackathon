import tkinter as tk

def on_click():
    print("Button was clicked!")

root = tk.Tk()
root.title("Tkinter Button Example")
root.geometry("300x200")

button = tk.Button(root, text="biology", command=on_click)

button.pack(pady=20)
root.mainloop()
