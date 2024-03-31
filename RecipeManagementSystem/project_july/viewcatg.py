from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import connection

class view:
    def __init__(self):
        self.mainlbcolour = "#CFCCD6"
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title("View Category")
        self.root.configure(bg="#AD9BAA")

        self.mainLabel = Label(self.root, text="View Category", font=('', 30, 'bold'), bg="#CFCCD6")
        self.mainLabel.pack(pady=20, ipadx=10, ipady=10)

        self.mainLabel = Label(self.root, text="View Category", font=('', 30, 'bold'), bg="#CFCCD6")
        self.mainLabel = Label(self.root, text="View Category", font=('', 30, 'bold'), bg="#CFCCD6")
        self.formFrame = Frame(self.root, bg="#CFCCD6")
        self.formFrame.pack(pady=10)

        self.lb = Label(self.formFrame, text="Search by Name,Description", font=('arial', 18),bg="#CFCCD6")
        self.txt = Entry(self.formFrame, font=('arial', 18))
        self.bt1 = Button(self.formFrame, text="Search", font=('arial', 18), command=self.searchCategory,
                          highlightthickness=5, relief=RAISED)
        self.bt2 = Button(self.formFrame, text="Refresh", font=('arial', 18), command=self.getValues,
                          highlightthickness=5, relief=RAISED)
        self.lb.grid(row=0, column=0, padx=10)
        self.txt.grid(row=0, column=1, padx=10)
        self.bt1.grid(row=0, column=2, padx=10)
        self.bt2.grid(row=0, column=3, padx=10)

        self.ct = ttk.Treeview(self.root, columns=('name', 'description'))
        self.ct.pack(pady=20, padx=20, expand=True, fill='both')
        self.ct.heading('name', text="Name")
        self.ct.heading('description', text="Description")

        self.ct['show'] = 'headings'
        self.getValues()
        style = ttk.Style()
        style.configure('Treeview', font=('arial', 18, 'bold'), rowheight=40)
        style.configure('Treeview.Heading', font=('arial', 20, 'bold'))

        self.delete = Button(self.root, text="Delete", width=25, font=('', 18), command=self.deleteCatg,
                             highlightthickness=5, relief=RAISED)
        self.delete.pack(pady=20)

        self.root.mainloop()

    def searchCategory(self):
            search = self.txt.get()
            q = f"select * from category where name like '%{search}%' or description like '%{search}%'"
            self.cr.execute(q)
            data = self.cr.fetchall()
            print(self.ct.get_children())
            for row in self.ct.get_children():
                self.ct.delete(row)
            count = 0
            for i in data:
                self.ct.insert('', index=count, values=i)
                count += 1

    def getValues(self):
        self.conn = connection.Connect()
        self.cr = self.conn.cursor()
        q = "select name,description from category"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for row in self.ct.get_children():
            self.ct.delete(row)
        count =0
        for i in data:
            self.ct.insert('', index=count, values=i)
            count += 1

    def deleteCatg(self):
           rowid = self.ct.selection()
           if len(rowid)==0:
            msg.showwarning("WARNING", "Please select a row", parent=self.root)
           elif len(rowid)>1:
            msg.showwarning("WARNING", "Please selecta single row", parent=self.root)
           else:
            items = self.ct.item(rowid[0])
            data = items['values']
            q = f"delete from category where name ='{data[0]}'"
            self.cr.execute(q)
            self.conn.commit()
            self.getValues()
            msg.showinfo("Success", "Category has been removed", parent=self.root)

if __name__ == '__main__':
    obj = view()

