from tkinter import *
import parser
import os

root = Tk()
root.title('Computer Networks')
root.configure(bg='black')

#get the user input and place it in the textfield
i = 0
def get_variables(num):
    global i
    i+=1

#adding buttons to the calculator

def generatepacket():
    os.system('python3 gpacket.py')

def wireshark():
    os.system('python3 wire.py')

def secret():
    os.system('python3 wire2.py')

def etherape():
    os.system('python3 etherape.py')

a=Button(root,text="Generate packet",height = 3, width = 20, command= generatepacket)
b=Button(root,text="Wireshark",height = 3, width = 20, command= wireshark)
d=Button(root,text="Secret",height = 3, width = 20, command= secret)
e=Button(root,text="EtherApe",height = 3, width = 20, command= etherape)
a.place(relx=0.2, rely=0.5, anchor=CENTER)
b.place(relx=0.4, rely=0.5, anchor=CENTER)
d.place(relx=0.6, rely=0.5, anchor=CENTER)
e.place(relx=0.8, rely=0.5, anchor=CENTER)


root.mainloop()
