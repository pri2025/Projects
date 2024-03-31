import tkinter
from tkinter import *
import tkinter.messagebox as msg

from connection import Connect

import tkinter.ttk as ttk

class main:
    def __init__(self):
        self.root = Tk()
        self.root.title('View ratings')
        self.root.state('zoomed')
        self.root.configure(bg="#AD9BAA")

        self.lb = tkinter.Label(self.root, text='VIEW REVIEWS', font=('arial', 28), bg='#CFCCD6')
        self.lb.pack(pady=20, ipady=10, ipadx=10)

        self.formframe = tkinter.Frame(self.root, bg="#CFCCD6")
        self.formframe.pack()

        #h = ('arial', 15)
        self.lb = Label(self.formframe, text="Search by id, user id, recipe id, rating", font=('arial', 20))
        self.lb.grid(row=0, column=0)
        self.txt = tkinter.Entry(self.formframe, width=20)
        self.txt.grid(row=0, column=1, padx=20, ipady=10, ipadx=10)
        self.btn1 = tkinter.Button(self.formframe, text="Search", font=('arial', 18), command=self.search, width=8,
                                   highlightthickness=5, relief=RAISED)
        self.btn2 = tkinter.Button(self.formframe, text="Refresh", font=('arial', 18), command=self.getvalues, width=8,
                                   highlightthickness=5, relief=RAISED)
        self.btn1.grid(row=0, column=2, padx=20, ipady=10, ipadx=10)
        self.btn2.grid(row=0, column=3, padx=20, ipady=10, ipadx=10)

        self.table = ttk.Treeview(self.root, columns=('id', 'userid', 'recipeid', 'ratings', 'description'))
        self.table.pack(pady=10, expand=True, fill='both')
        self.btn = tkinter.Button(self.root, text="DELETE", width=15, command=self.delete, highlightthickness=5, relief=RAISED)
        self.btn.pack(pady=10, ipady=20, ipadx=20)
        self.table.heading('id', text="ID")
        self.table.heading('userid', text="USER ID")
        self.table.heading('recipeid', text="RECIPE ID")
        self.table.heading('ratings', text="RATINGS")
        self.table.heading('description', text="REVIEW")
        self.table['show'] = 'headings'

        self.getvalues()

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 18, 'bold'), rowheight=40)
        style.configure('Treeview.Heading', font=('', 20, 'bold'), rowheight=40)

        self.root.mainloop()

    def getvalues(self):
        self.conn= Connect()
        self.cr= self.conn.cursor()
        q = "select id, userid, recipeID, ratings, review from ratings"
        print(q)
        self.cr.execute(q)

        data = self.cr.fetchall()
        for row in self.table.get_children():
            self.table.delete(row)
        c = 0
        for i in data:
            self.table.insert('', index=c, values=i)
            c += 1

    def search(self):
        self.conn = Connect()
        self.cr= self.conn.cursor()
        s = self.txt.get()
        print(s)
        q = f"select * from ratings where ratings like '%{s}%' or userid like '%{s}%' or recipeid like '%{s}%'or id like '%{s}%'"
        print(q)
        self.cr.execute(q)
        data = self.cr.fetchall()

        for row in self.table.get_children():
            self.table.delete(row)
        c = 0
        for i in data:
            self.table.insert('', index=c, values=i)
            c += 1

    def delete(self):
        rowid = self.table.selection()
        if len(rowid) == 0:
            msg.showinfo('', "Select a row!", parent=self.root)
        elif len(rowid) > 1:
            msg.showinfo('', "Please select only one row at a time!!", parent=self.root)
        else:
            items = self.table.item(rowid[0])
            data = items['values']
            q = f"delete from ratings where id='{data[0]}'"
            self.cr.execute(q)
            self.conn.commit()
            self.getvalues()
            msg.showinfo('', "Row Deleted", parent=self.root)

if __name__ == '__main__':
    x = main()