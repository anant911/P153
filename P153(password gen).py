#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 20:45:21 2022

@author: AnantSrivastava
"""

from tkinter import*
import random
root=Tk()
root.title("pass")
root.geometry("600x600")

enter=Entry(root)
lbl=Label(root)
lb2=Label(root)

array_3d=[[['1','2','3','4','5','6','7','8','9','10'],["anAnt","casPer","iphoNe","YouTube","3d_Printer","doG","shOes","ihackU"],['!','@','#','$','%','^','&','*','(',')']]]

def GEN():
    lbl["text"]="guessed password: "+enter.get()
    
    ran1=random.randint(0,9)
    ran2=random.randint(0,7)
    ran3=random.randint(0,9)
    
    let1=str(array_3d[0][0][ran1])
    let2=(array_3d[0][1][ran2])
    let3=(array_3d[0][2][ran3])
    lb2["text"]="created password: "+let1+let2+let3


btn=Button(root, text="new password",command=GEN)
enter.place(relx=0.5, rely=0.4, anchor=CENTER)
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
btn.place(relx=0.5, rely=0.6, anchor=CENTER)
lb2.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()