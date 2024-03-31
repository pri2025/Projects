import tkinter
import tkinter.messagebox as msg  #alias
import tkinter.ttk as ttk
from connection import Connect
import dashboard
class main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Admin Login')
        self.root.geometry('600x600')
        self.root.configure(bg="#CFDBD5")

        self.mainlabel = tkinter.Label(self.root, text="Admin Login", font=('arial', 28, 'bold'), bg="#E8EDDF")
        self.mainlabel.pack(pady=20, ipadx=30, ipady=20)

        self.formFrame = tkinter.Frame(self.root, bg="#E8EDDF")
        self.formFrame.pack()
        self.font = ("arial", 16)

        self.lb1 = tkinter.Label(self.formFrame, text="Enter Email", font=self.font, bg="#E8EDDF")
        self.txt1 = tkinter.Entry(self.formFrame, font=self.font, width=30)
        self.lb1.grid(row=0, column=0, pady=15, padx=10)
        self.txt1.grid(row=0, column=1, pady=15, padx=10)

        self.lb2 = tkinter.Label(self.formFrame, text="Enter Password", font=self.font, bg="#E8EDDF")
        self.txt2 = tkinter.Entry(self.formFrame, font=self.font, width=30, show='*')
        self.lb2.grid(row=1, column=0, pady=15, padx=10)
        self.txt2.grid(row=1, column=1, pady=15, padx=10)


        self.btn = tkinter.Button(self.root, text="Login", width=25, font=("arial", 14), command =self.Check,
                                  highlightthickness=5, relief=tkinter.RAISED)
        self.btn.pack(pady=10)

        self.root.mainloop()

    def Check(self):
        email = self.txt1.get()
        password = self.txt2.get()
        conn = Connect()
        cr = conn.cursor()
        q = f"select * from admin where email='{email}' and password='{password}'"
        cr.execute(q)
        result = cr.fetchall()
        print(result)
        if len(result) == 0:
            msg.showwarning("WARNING", "Invalid email/password", parent=self.root)
        else:
            msg.showinfo("SUCCESS", "Login successful", parent=self.root)
            self.root.destroy()
            email=result[0][2]
            role=result[0][-1]
            name=result[0][1]
            dashboard.Main(ID=result[0][0], adminname=name, adminemail=email, adminrole=role)

if __name__ == '__main__':
    obj = main()