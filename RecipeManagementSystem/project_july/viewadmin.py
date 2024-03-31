from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import connection

class Main:
    def __init__(self):
        self.mainlbcolour = "#CFCCD6"
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('View Admin')
        self.root.configure(bg="#AD9BAA")

        self.mainLabel = Label(self.root, text="View Admin", font=('', 28, 'bold'),
                               bg=self.mainlbcolour, foreground="Black")

        self.mainLabel.pack(pady=20,  ipadx=20, ipady=20)

        self.formFrame = Frame(self.root, bg="#CFCCD6")
        self.formFrame.pack(pady=10)

        self.lb = Label(self.formFrame, text="Search by Name,Email", font=('arial', 14))
        self.txt = Entry(self.formFrame, font=('arial', 14))
        self.bt1 = Button(self.formFrame, text="Search", font=('arial', 14), command=self.searchAdmin,
                          highlightthickness=5, relief=RAISED)
        self.bt2 = Button(self.formFrame, text="Refresh", font=('arial', 14), command=self.getValues,
                          highlightthickness=5, relief=RAISED)
        self.lb.grid(row=0, column=0, padx=10)
        self.txt.grid(row=0, column=1, padx=10)
        self.bt1.grid(row=0, column=2, padx=10)
        self.bt2.grid(row=0, column=3, padx=10)

        self.adminTable = ttk.Treeview(self.root, columns=('id', 'name', 'email', 'mobile', 'role'))
        self.adminTable.pack(pady=20, padx=20, expand=True, fill='both')
        self.adminTable.heading('id', text="ID")
        self.adminTable.heading('name', text="Name")
        self.adminTable.heading('email', text="Email")
        self.adminTable.heading('mobile', text="Mobile")
        self.adminTable.heading('role', text="Role")
        self.adminTable['show'] = 'headings'
        self.getValues()
        style = ttk.Style()
        style.configure('Treeview', font=('arial', 18), rowheight=40)
        style.configure('Treeview.Heading', font=('arial', 20, 'bold'))
        self.adminTable.bind("<Double-1>", self.openUpdateWindow)

        self.delete = Button(self.root, text="Delete", width=20, font=('', 18), command=self.deleteadmin,
                             highlightthickness=5, relief=RAISED)
        self.delete.pack(pady=30)

        self.root.mainloop()

    def searchAdmin(self):
        search = self.txt.get()
        q = f"select id,name,email,mobile,role from admin where name like '%{search}%' or email like '%{search}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()
       # print(self.adminTable.get_children())
        for row in self.adminTable.get_children(): #treeview ki jitni rows utne children, get_children returns all the rows
            self.adminTable.delete(row)
        count = 0
        for i in data:
            self.adminTable.insert('', index=count, values=i)
            count += 1


    def getValues(self):
        self.conn = connection.Connect()
        self.cr = self.conn.cursor()
        q = "select id,name,email,mobile,role from admin"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for row in self.adminTable.get_children():
            self.adminTable.delete(row)    #taki refresh krne pr searched row delete ho jaye
        count = 0
        for i in data:
            self.adminTable.insert('', index=count, values=i)
            count += 1
    def deleteadmin(self):
        rowid = self.adminTable.selection() #jis row/s ko select kra uski id return krega in form of tuple
        if len(rowid) == 0:
            msg.showwarning("warning", "Please select a row", parent=self.root)
        elif len(rowid) > 1:
            msg.showwarning("Warning", "please select a single row", parent=self.root)
        else:
            items = self.adminTable.item(rowid[0])
            #fetches item of selected rows in treeview #rowid ke zero index pr id hai
            data = items['values']
            q = f"delete from admin where id ='{data[0]}'"
            self.cr.execute(q)
            self.conn.commit()
            self.getValues()
            msg.showinfo("Success", "Admin has been removed", parent=self.root)

    def openUpdateWindow(self, event):
        data = self.adminTable.item(self.adminTable.selection()[0])['values']
        #row id pass kri self.adminTable.selection ko #items ek dictionary hai jismein se values nikal li
        self.root1 = Toplevel()
        self.root1.title('Update Admin')
        self.root1.geometry('800x800')
        self.root1.configure(bg="#AD9BAA")
        font = ('', 18)
        self.label = Label(self.root1, text="Update Admin", font=('', 24, 'bold'), bg="#CFCCD6")
        self.label.pack(pady=20)

        self.frame = Frame(self.root1, bg="#CFCCD6")
        self.frame.pack(pady=10)

        self.lb1 = Label(self.frame, text="Admin ID", font=font, bg="#CFCCD6")
        self.txt1 = Entry(self.frame, font=font, width=30)
        self.lb1.grid(row=0, column=0, pady=20, padx=10)
        self.txt1.grid(row=0, column=1, pady=20, padx=10)
        self.txt1.insert(0, data[0]) #jo row select krenge uski id milegi jo zero likha hai vo zero index pr print krvaya
        self.txt1.configure(state='readonly') #taki koi id change na kr paye

        self.lb2 = Label(self.frame, text="Admin Name", font=font, bg="#CFCCD6")
        self.txt2 = Entry(self.frame, font=font, width=30)
        self.lb2.grid(row=1, column=0, pady=20, padx=10)
        self.txt2.grid(row=1, column=1, pady=20, padx=10)
        self.txt2.insert(0, data[1])

        self.lb3 = Label(self.frame, text="Admin Email", font=font, bg="#CFCCD6")
        self.txt3 = Entry(self.frame, font=font, width=30)
        self.lb3.grid(row=2, column=0, pady=20, padx=10)
        self.txt3.grid(row=2, column=1, pady=20, padx=10)
        self.txt3.insert(0, data[2])

        self.lb4 = Label(self.frame, text="Admin Mobile", font=font, bg="#CFCCD6")
        self.txt4 = Entry(self.frame, font=font, width=30)
        self.lb4.grid(row=3, column=0, pady=20, padx=10)
        self.txt4.grid(row=3, column=1, pady=20, padx=10)
        self.txt4.insert(0, data[3])

        self.lb5 = Label(self.frame, text="Admin Role", font=font, bg="#CFCCD6")
        self.txt5 = ttk.Combobox(self.frame, font=font, width=28, values=['Super Admin', 'Admin'], state='readonly')
        self.lb5.grid(row=4, column=0, pady=10, padx=10)
        self.txt5.grid(row=4, column=1, pady=10, padx=10)
        self.txt5.set(data[4]) #multiple values ko set krte insert nhi

        self.btn = Button(self.root1, text="UPDATE", width=15, font=font, command=self.update,
                          highlightthickness=5, relief=RAISED)
        self.btn.pack(pady=20)

    def update(self):
        id = self.txt1.get()
        name = self.txt2.get()
        email = self.txt3.get()
        mobile = self.txt4.get()
        role = self.txt5.get()

        q = f"update admin set name='{name}', email='{email}', mobile='{mobile}'," \
            f"role='{role}' where id = '{id}'"
        self.cr.execute(q)
        self.conn.commit()
        self.getValues()
        self.root1.destroy() #after update destoy window
        msg.showinfo("SUCCESS", "Admin has been updated", parent=self.root)


        self.root1.mainloop()
if __name__ == '__main__':
    obj = Main()


 # what are events?  clicking left side of mouse(bt1) , scrolling(bt2), clicking right side(bt3)
 #double-1 represents left click two times
 #TK is a class in tkinter used for creating main window of an application, cannot be used twice
 #then we use toplevel(), for ek or window
