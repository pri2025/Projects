from tkinter import *
import tkinter.messagebox as msg
from connection import Connect

class password:
    def __init__(self, adminemail):
        self.root = Tk()
        self.root.geometry("600x600")
        self.root.title("Password Change")
        self.root.configure(bg="#AD9BAA")

        self.mainLabel = Label(self.root, text="Change Password", font=('', 20, 'bold'), bg="#CFCCD6")
        self.mainLabel.pack(pady=20, ipady=10, ipadx=10)

        self.frame = Frame(self.root, bg="#CFCCD6")
        self.frame.pack()

        self.font = ('', 14)

        self.l1 = Label(self.frame, text="Email", font=self.font, bg="#CFCCD6")
        self.txt1 = Entry(self.frame, font=self.font, width=30)
        self.l1.grid(row=0, column=0, pady=20, padx=10)
        self.txt1.grid(row=0, column=1, pady=20, padx=10)
        self.txt1.insert(0,adminemail)
        self.txt1.configure(state="readonly")

        self.l2 = Label(self.frame, text="Old Password", font=self.font, bg="#CFCCD6")
        self.txt2 = Entry(self.frame, font=self.font, width=30)
        self.l2.grid(row=1, column=0, pady=20, padx=10)
        self.txt2.grid(row=1, column=1, pady=20, padx=10)

        self.l3 = Label(self.frame, text="New Password ", font=self.font, bg="#CFCCD6")
        self.txt3 = Entry(self.frame, font=self.font, width=30)
        self.l3.grid(row=2, column=0, pady=20, padx=10)
        self.txt3.grid(row=2, column=1, pady=20, padx=10)

        self.btn = Button(self.root, text="Submit", width=25,  font=self.font, command=self.Check,
                          highlightthickness=5, relief=RAISED)
        self.btn.pack(pady=20)
        self.root.mainloop()
    def Check(self):
        email = self.txt1.get()
        password = self.txt2.get()
        newpassword = self.txt3.get()
        conn = Connect()
        cr = conn.cursor()
        q = f"select * from admin where email='{email}' and password='{password}'"
        cr.execute(q)
        result = cr.fetchall()
        if len(result) == 0:
            msg.showwarning("WARNING", "Invalid email/password", parent=self.root)
        else:
            q = f"update admin set password='{newpassword}' where email = '{email}'"
            cr.execute(q)
            conn.commit()
            self.root.destroy()  # after update destroy window
            msg.showinfo("SUCCESS", "Password Updated")

if __name__ == '__main__':
    obj = password()

