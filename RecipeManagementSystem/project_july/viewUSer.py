from tkinter import *
import tkinter.messagebox as msg  #alias
import tkinter.ttk as ttk
import connection

class ViewUser:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('View User')
        self.root.configure(bg="#AD9BAA")

        self.mainLabel = Label(self.root, text="View User", font=('', 30, 'bold'), bg="#CFCCD6")
        self.mainLabel.pack(pady=20, ipady=10, ipadx=10)

        self.formFrame = Frame(self.root, bg="#CFCCD6")
        self.formFrame.pack(pady=10)

        self.lb = Label(self.formFrame, text="Search by Name,Email,Mobile,address", font=('arial', 18), bg="#CFCCD6")
        self.txt = Entry(self.formFrame, font=('arial', 18))
        self.bt1 = Button(self.formFrame, text="Search", font=('arial', 18), command=self.SearchUser,
                          highlightthickness=5, relief=RAISED)
        self.bt2 = Button(self.formFrame, text="Refresh", font=('arial', 18), command=self.getvalues,
                          highlightthickness=5, relief=RAISED)
        self.lb.grid(row=0, column=0, padx=10)
        self.txt.grid(row=0, column=1, padx=10)
        self.bt1.grid(row=0, column=2, padx=10)
        self.bt2.grid(row=0, column=3, padx=10)

        self.users = ttk.Treeview(self.root, columns=('id', 'name', 'email', 'mobile', 'gender', 'address'))
        self.users.pack(pady=20, padx=20, expand=True, fill='both')
        self.users.heading('id', text="ID")
        self.users.heading('name', text="Name")
        self.users.heading('email', text="Email")
        self.users.heading('mobile', text="Mobile")
        self.users.heading('gender', text="gender")
        self.users.heading('address', text="address")
        self.users['show'] = 'headings'
        self.getvalues()
        style = ttk.Style()
        style.configure('Treeview', font=('arial', 18), rowheight=40)
        style.configure('Treeview.Heading', font=('arial', 18, 'bold'))

        self.delete = Button(self.root, text="DELETE", font=('', 18), command=self.Delete,
                             highlightthickness=5, relief=RAISED)
        self.delete.pack(pady=10)

        self.users.bind("<Double-1>", self.openUpdateWindow)


        self.root.mainloop()

    def SearchUser(self):
        bucket = self.txt.get()
        q = f"select id,name,email,mobile,gender,address from user where name like '%{bucket}%'or email like '%{bucket}%'or mobile like '%{bucket}%'" \
            f"or address like '%{bucket}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for row in self.users.get_children():
            self.users.delete(row)
        count = 0
        for i in data:
            self.users.insert('', index=count, values=i)
            count += 1

    def getvalues(self):
        self.conn = connection.Connect()
        self.cr = self.conn.cursor()
        q = "select id,name,email,mobile,gender,address from user"
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for row in self.users.get_children():
            self.users.delete(row)
        count = 0
        for i in data:
            self.users.insert('', index=count, values=i)
            count += 1

    def Delete(self):
        rowid = self.users.selection()
        if len(rowid) == 0:
            msg.showwarning("WARNING", "Please select a row", parent=self.root)
        elif len(rowid) > 1:
            msg.showwarning("WARNING", "Please select a single row", parent=self.root)
        else:
            items = self.users.item(rowid[0])
            data = items['values']
            print(data)
            q = f"delete from user where id ='{data[0]}'"
            self.cr.execute(q)
            self.conn.commit()
            self.getvalues()
            msg.showinfo("Success", "Category has been removed")

    def openUpdateWindow(self, event):
        data = self.users.item(self.users.selection()[0])['values']
        self.root1 = Toplevel()
        self.root1.geometry('800x800')
        self.root1.configure(bg="#AD9BAA")
        self.root1.title("update")
        font = ('', 18)
        print(data)
        self.label = Label(self.root1, text="Update User", font=('', 24, 'bold'), bg="#CFCCD6")
        self.label.pack(pady=20)

        self.formFrame = Frame(self.root1)
        self.formFrame.pack(pady=10)

        self.lb1 = Label(self.formFrame, text="Uer ID", font=font, bg="#CFCCD6")
        self.txt1 = Entry(self.formFrame, font=font, width=30)
        self.lb1.grid(row=0, column=0, pady=20, padx=10)
        self.txt1.grid(row=0, column=1, pady=20, padx=10)
        self.txt1.insert(0, data[0])
        self.txt1.configure(state='readonly')

        self.lb2 = Label(self.formFrame, text="User Name", font=font, bg="#CFCCD6")
        self.txt2 = Entry(self.formFrame, font=font, width=30)
        self.lb2.grid(row=1, column=0, pady=20, padx=10)
        self.txt2.grid(row=1, column=1, pady=20, padx=10)
        self.txt2.insert(0, data[1])

        self.lb3 = Label(self.formFrame, text="User Email", font=font, bg="#CFCCD6")
        self.txt3 = Entry(self.formFrame, font=font, width=30)
        self.lb3.grid(row=2, column=0, pady=20, padx=10)
        self.txt3.grid(row=2, column=1, pady=20, padx=10)
        self.txt3.insert(0, data[2])

        self.lb4 = Label(self.formFrame, text="User Mobile", font=font, bg="#CFCCD6")
        self.txt4 = Entry(self.formFrame, font=font, width=30)
        self.lb4.grid(row=3, column=0, pady=20, padx=10)
        self.txt4.grid(row=3, column=1, pady=20, padx=10)
        self.txt4.insert(0, data[3])

        self.lb5 = Label(self.formFrame, text="Gender", font=font, bg="#CFCCD6")
        self.txt5 = Entry(self.formFrame, font=font, width=30)
        self.lb5.grid(row=4, column=0, pady=10, padx=10)
        self.txt5.grid(row=4, column=1, pady=10, padx=10)
        self.txt5.insert(0, data[4])

        self.lb6 = Label(self.formFrame, text="Address", font=font, bg="#CFCCD6")
        self.txt6 = Entry(self.formFrame, font=font, width=30)
        self.lb6.grid(row=5, column=0, pady=10, padx=10)
        self.txt6.grid(row=5, column=1, pady=10, padx=10)
        self.txt6.insert(0, data[5])

        self.submit= Button(self.root1, text="UPDATE", width=15, font=('', 16), command=self.update,
                            highlightthickness=5, relief=RAISED)
        self.submit.pack(pady=20)


    def update(self):
        id = self.txt1.get()
        name = self.txt2.get()
        email = self.txt3.get()
        mobile = self.txt4.get()
        gender = self.txt5.get()
        address = self.txt6.get()

        q = f"update user set name='{name}', email='{email}', mobile='{mobile}'," \
            f"gender='{gender}', address='{address}' where id = '{id}'"
        self.cr.execute(q)
        self.conn.commit()
        self.getvalues()
        self.root1.destroy()
        msg.showinfo("SUCCESS", "User has been updated", parent=self.root)

        self.root1.mainloop()

if __name__ == '__main__':
    object = ViewUser()

