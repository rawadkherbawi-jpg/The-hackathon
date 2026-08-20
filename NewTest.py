import tkinter as tk
from os.path import split

Subjects = {
    "math": ["geometry_https://www.youtube.com/watch?v=Aq5WXmQQooo", "algebra_https://www.youtube.com/watch?v=z7rxl5KsPjs&list=RDz7rxl5KsPjs&start_radio=1&pp=oAcB"]
}



def on_click(LinkLesson):
    import webbrowser
    print(f"You clicked button Geometry")
    # webbrowser.open(LinkLesson)


def button_click():
    print(f"You clicked button Math")
    # root = tk.Tk()
    Lesson = Subjects["math"][0].split("_")
    root.title("Math Sections")
    titleLesson = Lesson[0]
    LinkLesson = Lesson[1]
    # global titleLesson, LinkLesson
    root.geometry("800x500")
    buttonMath.place(x = 10000, y = 50000)
    buttonGeo = tk.Button(root, text="Geometry", command=on_click(LinkLesson))
    buttonGeo.pack(pady=50)
    root.mainloop()


root = tk.Tk()
root.title("Tkinter Button Example")
root.geometry("800x500")
buttonMath = tk.Button(root, text="math", command=button_click)
buttonMath.pack(pady=20)

root.mainloop()