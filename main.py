from tkinter import *
import math
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
np.random.shuffle(arr)
strval = ''
num = "4279"

def click (value):
    button[value-1].config(bg='yellow')
    global strval
    strval += str(arr[value-1])

def verify(num):
    feild.delete(0, END)
    if(num==strval):
        global f
        feild.insert(0,"Successful")
    else:
        feild.insert(0,"Unsuccessful")


root=Tk()
root.title("Image Based Captcha")
root.config(bg="grey")
root.geometry("300x335")
root.resizable(False, False)

btn_img = []
button = []

c = 1
for i in arr:
    img = PhotoImage(file=f'set1/{i}.png')
    btn_img.append(img)
    button.append(Button(root,width=70,height=70,bd=10,image = btn_img[c-1],command=lambda button = c : click(button)))
    c+=1

c=0
for i in range(3):
    for j in range(3):
        button[c].grid(row=i,column=j,padx=5, pady=5)
        c+=1

feild = Entry(root,font=("arial",10,"bold"),relief=SUNKEN,width=14)
feild.grid(row=4,column=1,columnspan=1)
feild.insert(0,"Type : "+num)
Button(root,width=7,height=1, bg="green",bd=1,text="Verify",command=lambda: verify(num)).grid(row=4,column=2)

root.mainloop()