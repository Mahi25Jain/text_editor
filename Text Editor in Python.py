
from statistics import mode
from tkinter.filedialog import *
import tkinter as tk

def savefile():
    new_file = asksaveasfile(mode ='w', filetypes=[('text files', '.txt')])
    if new_file is None:
        return
    text =str(entry.get (1.0, tk.END))
    new_file.wrte(text)
    new_file.close()
    
def openfile():
    file = askopenfile(mode ='r', filetypes= [('text file','*.txt')])
    if file is not None:
        content = file.read()
    entry.insert(tk.INSERT,content )   
def clearFile():
    entry.delete(1.0,tk.END)

canvas = tk.Tk()
canvas.geometry("600x600")
canvas.title('TextPad!')
canvas.config(bg ="white")
top = tk.Frame(canvas)
top.pack(padx = 20 ,pady = 10 , anchor='nw')

b1 = tk.Button(canvas,text="Open" , bg ="white", command=openfile)
b1.pack(in_ =top,side="left")

b1 = tk.Button(canvas,text="Save" , bg ="white", command=savefile)
b1.pack(in_ =top,side="left")

b1 = tk.Button(canvas,text="Clear" , bg ="white",command=clearFile)
b1.pack(in_ =top,side="left")

b1 = tk.Button(canvas,text="Exit" , bg ="white",command=exit)
b1.pack(in_ =top,side="left")

entry = tk.Text(canvas,wrap="word" , bg="#F9DDA4" ,font =("poppins",16))
entry.pack(padx = 10 ,pady =5 ,expand= True ,fill= "both")



canvas.mainloop()