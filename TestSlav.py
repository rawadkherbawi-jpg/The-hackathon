import tkinter as tk

root = tk.Tk()
root.title("Grid of Buttons")

def button_click(number):
    print(f"You clicked button {LessonName}")

# Create and position 5 buttons dynamically in a row
buttons = []
ammountOfLessons = int(input("How many lessons would you like? "))
for i in range(ammountOfLessons):
    LessonName = input("Enter Lesson Name: ")
    btn = tk.Button(root, text=f"Button {LessonName}", command=lambda i=i: button_click(i+1))
    btn.grid(row=0, column=i, padx=5, pady=5)
    buttons.append(btn)

root.mainloop()
#
#
#
# import tkinter as tk
# from os.path import split
#
# Subjects = {
#     "math": ["geometry_https://www.youtube.com/watch?v=Aq5WXmQQooo", "algebra_https://www.youtube.com/watch?v=z7rxl5KsPjs&list=RDz7rxl5KsPjs&start_radio=1&pp=oAcB"]
# }
#
#
#
# def on_click(LinkLesson):
#     import webbrowser
#     print(f"You clicked button Geometry")
#     # webbrowser.open(LinkLesson)
#
#
# def button_click():
#     print(f"You clicked button Math")
#     # root = tk.Tk()
#     Lesson = Subjects["math"][0].split("_")
#     root.title("Math Sections")
#     titleLesson = Lesson[0]
#     LinkLesson = Lesson[1]
#     # global titleLesson, LinkLesson
#     root.geometry("800x500")
#     buttonMath.place(x = 10000, y = 50000)
#     buttonGeo = tk.Button(root, text="Geometry", command=on_click(LinkLesson))
#     buttonGeo.pack(pady=50)
#     root.mainloop()
#
#
# root = tk.Tk()
# root.title("Tkinter Button Example")
# root.geometry("800x500")
# buttonMath = tk.Button(root, text="math", command=button_click)
# buttonMath.pack(pady=20)
#
# root.mainloop()