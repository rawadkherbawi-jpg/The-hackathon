import tkinter as tk
import customtkinter
app = customtkinter.CTk()
from PIL import Image
import PIL
from PIL import Image


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
    app.title("Math Sections")
    app.geometry("800x500")
    button1 = customtkinter.CTkButton(app, text="Geometry", command=on_click)
    button1.place(x = 600, y= 60)
    button1 = customtkinter.CTkButton(app, text="Algebra", command=on_click2)
    button1.place(x=600, y=110)
    app.mainloop()


def button_click1():
    app.title("Physics Sections")
    app.geometry("800x500")
    button1 = customtkinter.CTkButton(app, text="Mechanic", command=on_click1)
    button1.place(x = 350, y = 60)
    button3 = customtkinter.CTkButton(app, text="Electric", command=on_click3)
    button3.place(x=350, y=110)
    app.mainloop()

def science():
    button = customtkinter.CTkButton(app, text="physics", command=button_click1)
    button.place(x=100, y=60)

# app = customtkinter.CTk()
# app.title("Lesson Sections")
# app.geometry("800x500")
# bg_raw_image = Image.open("pastel-peach-orange-teal-blue-260nw-2437365889.jpg")
# bg_image = customtkinter.CTkImage(light_image=bg_raw_image, dark_image=bg_raw_image, size=(600, 400))
# bg_label = customtkinter.CTkLabel(app, text="", image=bg_image)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)
# def resize_background(event):
#     if event.widget == app:
#         new_image = customtkinter.CTkImage(light_image=bg_raw_image, dark_image=bg_raw_image, size=(event.width, event.height))
#         bg_label.configure(image=new_image)
# app.bind("<Configure>", resize_background)

# image = PIL.Image.open("pastel-peach-orange-teal-blue-260nw-2437365889.png")
# background_image = customtkinter.CTkImage(image, size=(500, 500))
#
# app.title("app")
# app.geometry("500x500")
#
#
# def bg_resizer(e):
#     if e.widget is app:
#         i = customtkinter.CTkImage(image, size=(e.width, e.height))
#         bg_lbl.configure(text="", image=i)
#
#
# # Create a bg label
# bg_lbl = customtkinter.CTkLabel(app, text="", image=background_image)
# bg_lbl.place(x=0, y=0)
#
# # Create a label
# label = customtkinter.CTkLabel(app, text="")
# label.pack(padx=20, pady=20)








button = customtkinter.CTkButton(app, text="math", command=button_click)
button.place(x = 600, y= 20)
button = customtkinter.CTkButton(app, text="physics", command=button_click1)
button.place(x = 350, y =20)
button = customtkinter.CTkButton(app, text="science", command=science)
button.place(x = 100, y =20)


app.mainloop()