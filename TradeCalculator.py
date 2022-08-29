from tkinter import *
from turtle import back
from unittest.util import three_way_cmp

root = Tk()

root.title('Ninja Calculator')



root.configure(background='black')
text1 = Label(root, text="Risk Calculator - CryptoNinjas", width=30,font="Bahnschrift",bg="black",foreground="white").grid(row=0, column =1)
textspace1 = Label(root, text=" ", width=30,font="Bahnschrift",bg="black",foreground="white").grid(row=0, column =2)
text2 = Label(root, text="Enter your USDT Stack Amount", pady=20,font="Bahnschrift",bg="black",foreground="white").grid(row=1,column=1)
textspace2 = Label(root, text=" ", width=30,font="Bahnschrift",bg="black",foreground="white").grid(row=1, column =2)
ent = Entry(root, width=20,font="Bahnschrift",bg="white",foreground="black")
ent.grid(row=2,column=1)
textspace3 = Label(root, text=" ", width=30,font="Bahnschrift",bg="black",foreground="white").grid(row=2, column =2)
textspace2 = Label(root, text=" ", width=30,font="Bahnschrift",bg="black",foreground="white").grid(row=3, column =2)
def myClick():
    one = 0.01 * float(ent.get())
    three = 0.03 * float(ent.get())
    five = 0.05 * float(ent.get())
    OnetoText = StringVar()
    OnetoText.set("Low-Risk 1%:         {:.2f}".format(one))
    ThreetoText = StringVar()
    ThreetoText.set("Medium-Risk 3%:        {:.2f}".format(three))
    FivetoText = StringVar()
    FivetoText.set("High-Risk 5%:           {:.2f}".format(five))
    textspace2 = Label(root, text="Amount = Stop loss: ", width=30,font="Bahnschrift",bg="black",foreground="white").grid(row=5, column =1)
    entryMagic = Entry(root, font="Bahnschrift",bd=0,state="readonly",readonlybackground="black",foreground="white",width=25, textvariable=OnetoText).grid(row=6,column=1)   
    entryMagic2 = Entry(root, font="Bahnschrift",bd=0,state="readonly",readonlybackground="black",foreground="white",width=25,bg="black",textvariable=ThreetoText).grid(row=7,column=1)   
    entryMagic3 = Entry(root, font="Bahnschrift",bd=0,state="readonly",bg="black",readonlybackground="black",foreground="white",width=25,textvariable=FivetoText).grid(row=8,column=1)   
    
  
    

myButton = Button(root, text="Calculate",font="Bahnschrift", padx=20, pady=20, command=myClick, bg="#1BBF4A",foreground="white").grid(row=4,column=1)
textspace4 = Label(root, text=" ", width=30,font="Bahnschrift",bg="black").grid(row=4, column =2)








root.mainloop()
