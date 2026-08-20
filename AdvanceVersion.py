import tkinter as tk
from os.path import split

Subjects = {
    "math": ["geometry_https://www.youtube.com/watch?v=Aq5WXmQQooo", "algebra_https://www.youtube.com/watch?v=z7rxl5KsPjs&list=RDz7rxl5KsPjs&start_radio=1&pp=oAcB"]
}
names = []
linls = []
for subject in Subjects:
    print(subject)
    for name in range(len(Subjects[subject])):
        NameAndLink = Subjects[subject][name]
        print(NameAndLink)
        SplitNameLink = NameAndLink.split("_")
        names.append(SplitNameLink[0])
        linls.append(SplitNameLink[1])

root = tk.Tk()
root.title("Lessons")
root.geometry("800x500")
ButtonsFirst = []
buttonsSecondary = []
print(names)
print(linls)

for lessons in range(len(Subjects)):
    btn = tk.Button(root, text=list(Subjects)[lessons], command=lambda i=lessons: button_click(i + 1))


def button_click(number):
    print(f"You clicked button {list(Subjects)[lessons]}")
    for i in range(len(names)):
        btn = tk.Button(root, text=names[i], command=lambda i=i: button_click(i + 1))
        btn.grid(row=0, column=i, padx=5, pady=5)
        buttonsSecondary.append(btn)


root.mainloop()