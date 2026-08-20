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