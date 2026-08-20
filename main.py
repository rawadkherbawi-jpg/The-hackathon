import tkinter as tk
def on_click():
    import webbrowser
    webbrowser.open("https://www.youtube.com/watch?v=UhgZBYtDE3Q&list=PL6LUMj1bhfm62DCHDEDK9f2iRSeNVBGb4&index=1")
root = tk.Tk()
root.title("Tkinter Button Example")
root.geometry("800x500")
button = tk.Button(root, text="biology", command=on_click)
button.pack(pady=20)
button1 = tk.Button(root, text="math", command=on_click)
button1.pack(pady=200)

root.mainloop()