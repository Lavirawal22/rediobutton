from tkinter import *
root=Tk()
root.geometry("600x450")
root.title("redio button tutorial")
var=IntVar()
var.set(1)
Label(root,text="What would you like to have sir?",font="lucida 19 bold",
      justify=LEFT,padx=14).pack()
List = [ 'Pizza', 'Boriyani', 'Fried Rice','Dosa','Idly','pow baji','Ice Crem','pani puri']
for i, item in enumerate(List):
    Radiobutton(root, text= item,padx=14,variable=var, value= i+1).pack(anchor='w')
radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value=1).pack()
radio=Radiobutton(root,text="Idly",padx=14,variable=var,value=2).pack()
radio=Radiobutton(root,text="pow baji",padx=14,variable=var,value=3).pack()
radio=Radiobutton(root,text="Ice Crem",padx=14,variable=var,value=4).pack()
radio=Radiobutton(root,text="pani puri",padx=14,variable=var,value=5).pack()


root.mainloop()