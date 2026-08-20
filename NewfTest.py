import tkinter as tk

def on_click():
    import webbrowser
    webbrowser.open("https://www.youtube.com/watch?v=Aq5WXmQQooo")

def on_click1():
    import webbrowser
    webbrowser.open("https://www.youtube.com/watch?v=ZAqIoDhornk")

def on_click2():
    import webbrowser
    webbrowser.open("https://www.youtube.com/watch?v=NybHckSEQBI&pp=ygUMYWxnZWJyYSBtYXRo")

def on_click3():
    import webbrowser
    webbrowser.open("https://www.youtube.com/watch?v=r-SCyD7f_zI")


def on_click4():
     import webbrowser
     webbrowser.open("https://www.youtube.com/watch?v=3tisOnOkwzo")



def button_click():
    root.title("Math Sections")
    root.geometry("800x500")
    button1 = tk.Button(root, text="Geometry", command=on_click)
    button1.place(x = 390, y= 60)
    button1 = tk.Button(root, text="Algebra", command=on_click2)
    button1.place(x=390, y=110)
    root.mainloop()


def button_click1():
    root.title("Physics Sections")
    root.geometry("800x500")
    button1 = tk.Button(root, text="Mechanic", command=on_click1)
    button1.place(x = 295, y = 60)
    button3 = tk.Button(root, text="Electric", command=on_click3)
    button3.place(x=295, y=110)
    root.mainloop()

def science():
    button = tk.Button(root, text="physics", command=button_click1)
    button.place(x=300, y=20)


root = tk.Tk()
root.title("Tkinter Button Example")
root.geometry("800x500")
button = tk.Button(root, text="math", command=button_click)
button.place(x = 400, y= 20)
button = tk.Button(root, text="physics", command=button_click1)
button.place(x = 300, y =20)
button = tk.Button(root, text="science", command=science)
button.place(x = 200, y =20)


root.mainloop()