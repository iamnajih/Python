from tkinter import*
from tkinter.filedialog import asksaveasfilename
import qrcode
from PIL import ImageTk, Image

root=Tk()
root.geometry("1000x800")
root.title("QR Code Maker")
root.config(bg='#121212')

def create():
    dataqr=data.get()
    img=qrcode.make(dataqr)
    path=asksaveasfilename(filetypes=[('Image','*.jpg',), ('All','*.*')])
    img.save(path)
    image=Image.open(path)
    photo=ImageTk.PhotoImage(image)
    label_image.config(image=photo,width=5000,height=5000)

Label(root,text="Enter What You Wanna Put It On   ",bg='#121212',fg='#fff').pack(side=TOP,padx=10,pady=20)
data=StringVar()
Entry(root,textvariable=data,bg='#1d1b1f',fg='#fff',justify=CENTER,insertbackground='#fff').pack(padx=10,pady=20)
Button(root,text="CREATE",bg='#000',fg='#3ef1f7',command=create).pack(padx=10,pady=20)
labelimage=Label(root,bg='#121212')
labelimage.pack(padx=10,pady=20)
root.mainloop()
