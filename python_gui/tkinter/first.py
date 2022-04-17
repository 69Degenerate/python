from logging import root
import tkinter as tk

root=tk.Tk()
c=tk.Canvas(root,width=500,height=200)
c.grid(columnspan=3)

line="Just Die"
label=tk.Label(root,text=line,font='Areal')
label.grid(column=1,row=0)

def define():
    butt.set('killed')
    t='not dead yet'
    tex=tk.Text(root,height=14,width=60,padx=10,pady=10)
    tex.insert(1.0,t)
    tex.tag_configure('center',justify='center')
    tex.tag_add('center',1.0,'end')
    tex.grid(column=1,row=2)

butt=tk.StringVar()
buton=tk.Button(root,textvariable=butt,command=lambda:define(),bg='red',height=3,width=6)
butt.set('kill')
buton.grid(column=1,row=1)



c=tk.Canvas(root,width=500,height=200)
c.grid(columnspan=3)


root.mainloop()
