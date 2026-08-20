import tkinter as tk
import webbrowser
def on_click():
    webbrowser.open("https://www.youtube.com/watch?v=UhgZBYtDE3Q&list=PL6LUMj1bhfm62DCHDEDK9f2iRSeNVBGb4&index=1")
root = tk.Tk()
root.title("Tkinter Button Example")
root.geometry("800x500")
button = tk.Button(root, text="biology", command=on_click)
button.place(x = 300, y = 20)
button1 = tk.Button(root, text="math", command=on_click)
button1.place(x = 400, y = 20)
button2 = tk.Button(root, text="physics", command=on_click)
button2.place(x = 500, y = 20)
root.mainloop()