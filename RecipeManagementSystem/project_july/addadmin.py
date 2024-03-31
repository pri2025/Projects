import tkinter
import tkinter.messagebox as msg  #alias
import tkinter.ttk as ttk
from connection import Connect

class main:
    def __init__(self):
        self.mainlbcolour = "#CFCCD6"
        self.root = tkinter.Tk()
        self.root.title('Add Admin')
        self.root.geometry('600x600')
        self.root.configure(bg="#AD9BAA")

        self.mainlabel = tkinter.Label(self.root, text="Add Admin", font=('arial', 28, 'bold'), bg=self.mainlbcolour,
                                       foreground="Black")#938BA1
        self.mainlabel.pack(pady=20, ipadx=20, ipady=20)

        self.formFrame = tkinter.Frame(self.root, bg="#CFCCD6")
        self.formFrame.pack()
        self.font = ("arial", 14)

        self.lb1 = tkinter.Label(self.formFrame, text="Enter Name", font=self.font, bg="#CFCCD6")
        self.txt1 = tkinter.Entry(self.formFrame, font=self.font, relief=tkinter.SOLID)
        self.lb1.grid(row=0, column=0, pady=15, padx =10)
        self.txt1.grid(row=0, column=1, pady=15, padx=10)

        self.lb2 = tkinter.Label(self.formFrame, text="Enter Email", font=self.font, bg="#CFCCD6")
        self.txt2 = tkinter.Entry(self.formFrame, font=self.font, relief=tkinter.SOLID)
        self.lb2.grid(row=1, column=0, pady=15, padx=10)
        self.txt2.grid(row=1, column=1, pady=15, padx=10)

        self.lb3 = tkinter.Label(self.formFrame, text="Enter Mobile", font=self.font, bg="#CFCCD6")
        self.txt3 = tkinter.Entry(self.formFrame, font=self.font, relief=tkinter.SOLID)
        self.lb3.grid(row=2, column=0, pady=15, padx=10)
        self.txt3.grid(row=2, column=1, pady=15, padx=10)

        self.lb4 = tkinter.Label(self.formFrame, text="Enter Password", font=self.font, bg="#CFCCD6")
        self.txt4 = tkinter.Entry(self.formFrame, font=self.font, relief=tkinter.SOLID)
        self.lb4.grid(row=3, column=0, pady=15, padx=10)
        self.txt4.grid(row=3, column=1, pady=15, padx=10)

        self.lb5 = tkinter.Label(self.formFrame, text="choose role", font=self.font, bg="#CFCCD6")
        self.txt5 = ttk.Combobox(self.formFrame, values=["super admin", "admin"] , state = "readonly",font=self.font)
        self.lb5.grid(row=4, column=0, pady=15, padx=10)
        self.txt5.grid(row=4, column=1, pady=15, padx=10)

        self.btn = tkinter.Button(self.root, text="submit", width=25, font=("arial", 14), command=self.insert,
                                  background="white", foreground="black", activebackground="white", activeforeground="black",
                                  highlightthickness=5, relief=tkinter.RAISED)
        self.btn.pack(pady=10)

        self.root.mainloop()

    def insert(self):
        name= self.txt1.get()
        email = self.txt2.get()
        mobile = self.txt3.get()
        password = self.txt4.get()
        role = self.txt5.get()
        if name == '' or email == '' or mobile == '' or password == '' or role == '':
            msg.showwarning("warning" , "please enter all values")
        else:
            conn = Connect()
            cr = conn.cursor()

            q = f"insert into admin values(null, '{name}','{email}','{mobile}','{password}','{role}')"

            cr.execute(q)
            conn.commit()
            msg.showwarning("success", "Admin added")
if __name__ == '__main__':
      obj = main()