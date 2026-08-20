import tkinter as tk
import customtkinter
app = customtkinter.CTk()
from PIL import Image
import PIL
from PIL import Image


def on_click():
    import webbrowser
    webbrowser.open("https://www.youtube.com/watch?v=k5etrWdIY6o&list=PLUPEBWbAHUsxuIbsAS--B6cobarm2bty2")


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


def on_click5():
    import webbrowser
    webbrowser.open("https://www.youtube.com/watch?v=5iTOphGnCtg")


def on_click6():
    import webbrowser
    webbrowser.open("https://www.youtube.com/watch?v=y2kg3MOk1sY")


def on_click7():
    import webbrowser
    webbrowser.open("youtube.com/watch?v=VtgB2pCC73M&pp=ygUOYXJ0cyBiZWdpbm5lcnM%3D")


def on_click8():
    import webbrowser
    webbrowser.open("https://www.youtube.com/watch?v=ht9GwXQMgpo")


def idea():
    idea_list = []
    root = tk.Tk()
    tk.Label(root, text="class").grid(row=0, column=0)
    entry1 = tk.Entry(root)
    entry1.grid(row=0, column=1)
    idea_list.append(entry1)
    exit = tk.Button(root, text="exit", command=root.destroy)
    exit.grid(row=0, column=2)


def button_click():
    app.title("Math Sections")
    app.geometry("1250x700")
    button1 = customtkinter.CTkButton(app, text="Geometry", command=on_click)
    button1.place(x = 510, y= 60)
    button1 = customtkinter.CTkButton(app, text="Algebra", command=on_click2)
    button1.place(x=510, y=100)
    app.mainloop()


def button_click1():
    app.title("Physics Sections")
    app.geometry("1250x700")
    button1 = customtkinter.CTkButton(app, text="Mechanic", command=on_click1)
    button1.place(x = 360, y = 90)
    button3 = customtkinter.CTkButton(app, text="Electric", command=on_click3)
    button3.place(x=360, y=130)
    app.mainloop()


def science():
    button = customtkinter.CTkButton(app, text="Physics", command=button_click1)
    button.place(x=360, y=50)
    button = customtkinter.CTkButton(app, text="Chemistry", command=on_click5)
    button.place(x=360, y=170)
    button = customtkinter.CTkButton(app, text="Biology", command=on_click4)
    button.place(x=360, y=200)

# app = tk.Tk()
app.title("Tkinter Button Example")
app.geometry("1000x700")
app.configure(fg_color="CadetBlue1")
button = customtkinter.CTkButton(app, text="Math", command=button_click)
button.place(x = 510, y= 20)
button = customtkinter.CTkButton(app, text="Science", command=science)
button.place(x = 360, y =20)
button = customtkinter.CTkButton(app, text="Technology", command=on_click6)
button.place(x = 210, y =20)
button = customtkinter.CTkButton(app, text="Arts", command=on_click7)
button.place(x = 60, y =20)
button = customtkinter.CTkButton(app, text="Engineering", command=on_click8)
button.place(x = 660, y =20)
button_idea = customtkinter.CTkButton(app, text="Session idea", command=idea)
button_idea.place(x = 810, y =20)
app.mainloop()
