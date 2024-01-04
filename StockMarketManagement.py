from tkinter import *
from  tkinter import  ttk
import  random

import csv
import  tkinter
import  pymysql
from  datetime import datetime
import numpy as np

root=Tk()
root.geometry("720x640")
root.title("Stoke Management System ")
root.resizable(False, False)
style=ttk.Style()
# define the TreeView
my_Tree=ttk.Treeview(root, show="headings", height=20)

placeholderArray=['','','','','']

for i in range(0,5):
    placeholderArray[i]=StringVar()

dumpydata=[[1,1,1,1,1,1,1],
[1,1,1,1,1,1]

           ]
def refreshTable():
    for data in my_Tree.get_children():
        my_Tree.delete(data)

    for array in dumpydata:
        my_Tree.insert(parent='',index=END,iid=array,text="",values=(array),tag='orow')
    my_Tree.tag_configure('orow',background='#EEEEEE')
    my_Tree.pack()

#Define the frame
frame=Frame(root, bg='#02577A')
frame.pack()


btncolor="#196E78"

# Manage Frame
manageframe=LabelFrame(frame, text="Manage",borderwidth=5)
manageframe.grid(row=0, column=0, sticky='w',padx=[10,200],pady=20,ipadx=[6])

#  Define Buttons

savebtn=Button(manageframe,text="SAVE",width=10,bg=btncolor, fg='white',borderwidth=3)
updatebtn=Button(manageframe,text="UPDATE",width=10,bg=btncolor, fg='white',borderwidth=3)
deletebtn=Button(manageframe,text="DELETE",width=10,bg=btncolor, fg='white',borderwidth=3)
selectbtn=Button(manageframe,text="SELECT",width=10,bg=btncolor, fg='white',borderwidth=3)
findbtn=Button(manageframe,text="FIND",width=10,bg=btncolor, fg='white',borderwidth=3)
clearbtn=Button(manageframe,text="CLEAR",width=10,bg=btncolor, fg='white',borderwidth=3)
exportbtn=Button(manageframe,text="EXPORT EXCEL ",width=15,bg=btncolor, fg='white',borderwidth=3)

# now Grid the buttons
savebtn.grid(row=0, column=0,padx=5,pady=5)
updatebtn.grid(row=0, column=1,padx=5,pady=5)
deletebtn.grid(row=0, column=2,padx=5,pady=5)
selectbtn.grid(row=0, column=3,padx=5,pady=5)
findbtn.grid(row=0, column=4,padx=5,pady=5)
clearbtn.grid(row=0, column=5,padx=5,pady=5)
exportbtn.grid(row=0, column=6,padx=5,pady=5)


# Make a new LabalFrame for Entries

entriesFrame=LabelFrame(frame, text="Form", borderwidth=5)
entriesFrame.grid(row=1,column=0, sticky='w',padx=[10,200],pady=[0,20],ipadx=[6])

# add the Labels

itemIdLabel=Label(entriesFrame, text=" ITEM ID", anchor='e',width=10)
nameLabel=Label(entriesFrame, text="NAME", anchor='e',width=10)
priceLabel=Label(entriesFrame, text="PRICE", anchor='e',width=10)
qntLabel=Label(entriesFrame, text="QNT", anchor='e',width=10)
categoryLabel=Label(entriesFrame, text="CATEGORY", anchor='e',width=10)

# NOW   GRID   all Labels

itemIdLabel.grid(row=0, column=0,padx=10)
nameLabel.grid(row=1, column=0,padx=10)
priceLabel.grid(row=2, column=0,padx=10)
qntLabel.grid(row=3, column=0,padx=10)
categoryLabel.grid(row=4, column=0,padx=10)

#values for Combobox
categoryArray=["Networking Tools","Computer Parts","Repair Tools","Gadgets"]

# Now add the Entry

itemIdEntry=Entry(entriesFrame, width=50, textvariable=placeholderArray[0])
nameEntry=Entry(entriesFrame, width=50, textvariable=placeholderArray[1])
priceEntry=Entry(entriesFrame, width=50, textvariable=placeholderArray[2])
qntEntry=Entry(entriesFrame, width=50, textvariable=placeholderArray[3])
categoryCombo=ttk.Combobox(entriesFrame, width=50, textvariable=placeholderArray[4], values=categoryArray)


# now Grid the Entry and Combobox
itemIdEntry.grid(row=0,column=2,pady=5,padx=5)
nameEntry.grid(row=1,column=2,pady=5,padx=5)
priceEntry.grid(row=2,column=2,pady=5,padx=5)
qntEntry.grid(row=3,column=2,pady=5,padx=5)
categoryCombo.grid(row=4,column=2,pady=5,padx=5)

#Buttons

generateIdBtn=Button(entriesFrame, text="GENERATE ID",borderwidth=3,bg=btncolor,fg='white')
generateIdBtn.grid(row=0,column=3,padx=5,pady=5)

style.configure(root)
# define the columns on Treeview
my_Tree['columns']=("Item Id","Name","Price","Quantity","Category","Date")

#formate the Treeview
my_Tree.column("#0",width=0,stretch=NO)
my_Tree.column("Item Id",anchor=W,width=70)
my_Tree.column("Name",anchor=W,width=125)
my_Tree.column("Price",anchor=W,width=125)
my_Tree.column("Quantity",anchor=W,width=100)
my_Tree.column("Category",anchor=W,width=150)
my_Tree.column("Date",anchor=W,width=150)


#category_array=['Network', 'Toots','Computer Tools', ]
#Define the Heading
my_Tree.heading("Item Id",text="Item Id",anchor=W)
my_Tree.heading("Name",text="Name",anchor=W)
my_Tree.heading("Price",text="Price",anchor=W)
my_Tree.heading("Quantity",text="Quantity",anchor=W)
my_Tree.heading("Category",text="Category",anchor=W)
my_Tree.heading("Date",text="Date",anchor=W)

my_Tree.tag_configure('orow',background="#EEEEEE")
my_Tree.pack()

refreshTable()
root.mainloop()
