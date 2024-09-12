from tkinter import*
from tkinter import filedialog
import os
root=Tk()
root.title("WebH")
root.geometry("600x400")

def openp():
    pro=filedialog.askopenfilename()
    os.system("pro")

button=Button(root, text="Open Program", command=openp)
button.pack(pady=20)
label=Label(root, text="")
label.pack(pady=20)
root.mainloop()
