from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect
import user_dashboard
class user:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("600x600")
        self.root.title("User Login")
        self.root.configure(bg="#CFDBD5")

        self.mainLabel = Label(self.root, text="User Login", font=('', 20, "bold"), bg="#E8EDDF")
        self.mainLabel.pack(pady=20, ipadx=10, ipady=10)

        self.frames = Frame(self.root, bg="#E8EDDF")
        self.frames.pack()
        self.font = ('', 16)

        self.l1 = Label(self.frames, text="EMAIL", font=self.font, bg="#E8EDDF")
        self.e1 = Entry(self.frames, font=self.font)
        self.l1.grid(row=0, column=0, pady=15, padx=10)
        self.e1.grid(row=0, column=1, pady=15, padx=10)

        self.l2= Label(self.frames, text="PASSWORD", font=self.font, bg="#E8EDDF")
        self.e2 = Entry(self.frames, font=self.font, show='*')
        self.l2.grid(row=1, column=0, pady=15, padx=10)
        self.e2.grid(row=1, column=1, pady=15, padx=10)

        self.btn = Button(self.root, text="Login", width=25, font=("arial", 18), command=self.Check,
                          highlightthickness=5, relief=RAISED)
        self.btn.pack(pady=10)

        self.root.mainloop()

    def Check(self):
        email = self.e1.get()
        password = self.e2.get()
        conn = Connect()
        cr = conn.cursor()
        q = f"select * from user where email='{email}' and password='{password}'"
        cr.execute(q)
        result = cr.fetchall()
        if len(result) == 0:
            msg.showwarning("WARNING", "Invalid email/password", parent=self.root)
        else:
            msg.showinfo("", 'LOGIN SUCCESSFUL', parent=self.root)
            self.root.destroy()
            user_dashboard.Main(userID=result[0][0], userName=result[0][1], userEmail=result[0][2])

if __name__ == '__main__':
    obj = user()


