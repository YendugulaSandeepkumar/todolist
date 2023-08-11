from tkinter import *
mw=Tk()
mw.geometry("400x500")
mw.resizable(False,False)

def add():
  task=e1.get()
  if task:
        listbox.insert(END, task)
        e1.delete(0,END)

def remove():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

def edit():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        selected_task_text = listbox.get(selected_task_index)
        e1.delete(0,END)
        e1.insert(0, selected_task_text)
        listbox.delete(selected_task_index)


lb1=Label(mw,text="TO-DO LIST",bg="orange",font="arial",width=38,height=5)
lb1.pack(padx=0,pady=10)
lb2=Label(mw,text="Add Items")
lb2.place(x=50,y=150)
lb3=Label(mw,text="Tasks")
lb3.place(x=40,y=220)

e1=Entry(mw,text="",width=20)
e1.place(x=20,y=180)

b1=Button(mw,text="Add",bg="skyblue",command=add,width=15,height=2)
b1.place(x=180,y=170)
b2=Button(mw,text="Edit",bg="green",command=edit,width=15,height=2)
b2.place(x=280,y=300)
b3=Button(mw,text="Delete",bg="red",command=remove,width=15,height=2)
b3.place(x=280,y=350)

listbox = Listbox(mw, selectmode=SINGLE,width=40,height=15)
listbox.place(x=10,y=250)


mw.mainloop()
