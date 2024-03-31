import tkinter
import tkinter.messagebox as msg  #alias
import tkinter.ttk as ttk
from connection import Connect

class category:
    def __init__(self):
        self.mainlbcolour = "#CFCCD6"
        self.root = tkinter.Tk()
        self.root.title('Add Category')
        self.root.geometry('600x600')
        self.root.configure(bg="#AD9BAA")

        self.mainlabel = tkinter.Label(self.root, text="Add Category", font=('arial', 28, 'bold'), bg=self.mainlbcolour,
                                       foreground="Black")
        self.mainlabel.pack(pady=20, ipadx=20, ipady=20)

        self.formFrame = tkinter.Frame(self.root, bg="#CFCCD6")
        self.formFrame.pack()
        self.font = ("arial", 14)

        self.lb1 = tkinter.Label(self.formFrame, text="Enter Name", font=self.font,  bg="#CFCCD6")
        self.txt1 = tkinter.Entry(self.formFrame, font=self.font, relief=tkinter.SOLID)
        self.lb1.grid(row=0, column=0, pady=15, padx=10)
        self.txt1.grid(row=0, column=1, pady=15, padx=10)

        self.lb2 = tkinter.Label(self.formFrame, text="Enter Description", font=self.font,  bg="#CFCCD6")
        self.txt2 = tkinter.Entry(self.formFrame, font=self.font, relief=tkinter.SOLID)
        self.lb2.grid(row=1, column=0, pady=15, padx=10)
        self.txt2.grid(row=1, column=1, pady=15, padx=10)

        self.btn = tkinter.Button(self.root, text="submit", width=25, font=("arial", 14), command=self.insert,
                                  highlightthickness=5, relief=tkinter.RAISED)
        self.btn.pack(pady=10)
        self.root.mainloop()
    def insert(self):
        name= self.txt1.get()
        description = self.txt2.get()
        if name == '' or description == '':
            msg.showwarning("warning", "please enter all values")
        else:
            conn = Connect()
            cr = conn.cursor()

            q = f"insert into category values('{name}','{description}')"

            cr.execute(q)
            conn.commit()
            msg.showwarning("success", "category added")

if __name__ == '__main__':
    obj = category()