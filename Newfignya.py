import tkinter as tk

def on_click():
    import webbrowser
    webbrowser.open("https://www.youtube.com/watch?v=Aq5WXmQQooo")


def button_click():
    print(f"You clicked button Math")
    # root = tk.Tk()
    root.title("Math Sections")
    root.geometry("800x500")
    button = tk.Button(root, text="Geometry", command=on_click)
    button.pack(pady=50)
    root.mainloop()


root = tk.Tk()
root.title("Tkinter Button Example")
root.geometry("800x500")
button = tk.Button(root, text="math", command=button_click)
button.pack(pady=20)

root.mainloop()