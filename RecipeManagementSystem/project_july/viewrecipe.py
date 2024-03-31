from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import Connect
from gtts import gTTS
import playsound
import threading
import os

class view:
    def __init__(self, userID):
        self.mainlbcolour = "#CFCCD6"
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('View Recipe')
        self.root.configure(bg="#AD9BAA")

        self.mainLabel = Label(self.root, text="View Recipe", font=('', 30, 'bold'),bg=self.mainlbcolour, foreground="Black")
        self.mainLabel.pack(pady=20, ipadx=20, ipady=20)

        self.formFrame = Frame(self.root, bg="#CFCCD6")
        self.formFrame.pack(pady=10)

        self.lb = Label(self.formFrame, text="Search by Name,Category,User", font=('arial', 18))
        self.txt = Entry(self.formFrame, font=('arial', 20))
        self.bt1 = Button(self.formFrame, text="Search", font=('arial', 18), command=self.searchRecipe,
                          highlightthickness=5, relief=RAISED)
        self.bt2 = Button(self.formFrame, text="Refresh", font=('arial', 18), command=self.getValues,
                          highlightthickness=5, relief=RAISED)
        self.lb.grid(row=0, column=0, padx=10)
        self.txt.grid(row=0, column=1, padx=10)
        self.bt1.grid(row=0, column=2, padx=10)
        self.bt2.grid(row=0, column=3, padx=10)

        self.table = ttk.Treeview(self.root, columns=('id', 'name', 'description', 'duration', 'ingredients',
                                                      'category', 'user'))
        self.table.pack(pady=20, padx=20, expand=True, fill='both')
        self.table.heading('id', text="ID")
        self.table.heading('name', text="Name")
        self.table.heading('description', text="Description")
        self.table.heading('duration', text="Duration")
        self.table.heading('ingredients', text="Ingredients")
        self.table.heading('category', text="Category")
        self.table.heading('user', text="User")
        self.table['show'] = 'headings'
        self.getValues()
        style = ttk.Style()
        style.configure('Treeview', font=('', 18, 'bold'), rowheight=40)
        style.configure('Treeview.Heading', font=('', 18, 'bold'))
        self.table.bind("<Double-1>", self.updateWindow)

        self.delete = Button(self.root, text="Delete", width=25, font=('', 18, 'bold'), command=self.deleteRecipe,
                             highlightthickness=5, relief=RAISED)
        self.delete.pack(pady=30)

        self.root.mainloop()

    def updateWindow(self, event):
        data = self.table.item(self.table.selection()[0])['values']
        # row id pass kri self.adminTable.selection ko #items ek dictionary hai jismein se values nikal li
        self.root1 = Toplevel()
        self.root1.title('Update Recipe')
        self.root1.geometry('800x800')
        self.root1.configure(bg="#AD9BAA")
        font = ('', 16)
        self.mainLabel = Label(self.root1, text="Update Recipe", font=('', 24, 'bold'),bg="#CFCCD6")
        self.mainLabel.pack(pady=20)

        self.formFrame = Frame(self.root1)
        self.formFrame.pack(pady=10)

        self.lb1 = Label(self.formFrame, text="ID", font=font, bg="#CFCCD6")
        self.txt1 = Entry(self.formFrame, font=font, width=30)
        self.lb1.grid(row=0, column=0, pady=15, padx=10)
        self.txt1.grid(row=0, column=1, pady=15, padx=10)
        self.txt1.insert(0, data[0])  # jo row select krenge uski id milegi jo zero likha hai vo zero index pr print krvaya
        self.txt1.configure(state='readonly')  # taki koi id change na kr paye

        self.lb2 = Label(self.formFrame, text="Name", font=font, bg="#CFCCD6")
        self.txt2 = Entry(self.formFrame, font=font, width=30)
        self.lb2.grid(row=1, column=0, pady=15, padx=10)
        self.txt2.grid(row=1, column=1, pady=15, padx=10)
        self.txt2.insert(0, data[1])

        self.lb3 = Label(self.formFrame, text="Description", font=font, bg="#CFCCD6")
        self.txt3 = Text(self.formFrame, font=font, height=10, width=30)
        self.lb3.grid(row=2, column=0, pady=15, padx=10)
        self.txt3.grid(row=2, column=1, pady=15, padx=10)
        self.txt3.insert('1.0', data[2])

        self.lb4 = Label(self.formFrame, text="Enter Duration", font=font, bg="#CFCCD6")
        self.txt4 = Entry(self.formFrame, font=font)
        self.lb4.grid(row=3, column=0, pady=15, padx=10)
        self.txt4.grid(row=3, column=1, pady=15, padx=10)
        self.txt4.insert(0, data[3])

        self.lb5 = Label(self.formFrame, text="Enter Ingredients", font=font, bg="#CFCCD6")
        self.txt5 = Entry(self.formFrame, font=font)
        self.lb5.grid(row=4, column=0, pady=15, padx=10)
        self.txt5.grid(row=4, column=1, pady=15, padx=10)
        self.txt5.insert(0, data[4])

        self.lb6 = Label(self.formFrame, text="Category", font=font, bg="#CFCCD6")
        self.txt6 = ttk.Combobox(self.formFrame, font=font, state='readonly', values=self.getCatName())
        self.lb6.grid(row=5, column=0, pady=15, padx=10)
        self.txt6.grid(row=5, column=1, pady=15, padx=10)
        self.txt6.insert(0, data[5])

        self.lb7 = Label(self.formFrame, text="User ID", font=font, bg="#CFCCD6")
        self.txt7 = Entry(self.formFrame, font=font)
        self.lb7.grid(row=6, column=0, pady=15, padx=10)
        self.txt7.grid(row=6, column=1, pady=15, padx=10)
        self.txt7.insert(0, data[-1])

        self.btn = Button(self.root1, text="UPDATE", width=15, font=font, command=self.update,
                          highlightthickness=5, relief=RAISED)
        self.btn.pack(pady=20)

        self.play = Button(self.root1, text="PLAY", width=15, font=font, highlightthickness=5, relief=RAISED,
                           command=lambda :threading.Thread(target=self.playText).start())
        self.play.pack()

    def deleteRecipe(self):
        rowid = self.table.selection()
        if len(rowid) == 0:
            msg.showwarning("warning", "Please select a row", parent=self.root)
        elif len(rowid) > 1:
            msg.showwarning("Warning", "please select a single row", parent=self.root)
        else:
            items = self.table.item(rowid[0])
            # fetches item of selected rows in treeview #rowid ke zero index pr id hai
            data = items['values']
            q = f"delete from recipe where id ='{data[0]}'"
            self.cr.execute(q)
            self.conn.commit()
            self.getValues()
            msg.showinfo("Success", "Recipe has been removed", parent=self.root)

    def searchRecipe(self):
        search = self.txt.get()
        q = f"select id,name,description,duration,ingredients,category,user from recipe where name like '%{search}%'" \
            f" or category like '%{search}%' or user like '%{search}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()
       # print(self.adminTable.get_children())
        for row in self.table.get_children(): #treeview ki jitni rows utne children, get_children returns all the rows
            self.table.delete(row)
        count = 0
        for i in data:
            self.table.insert('', index=count, values=i)
            count += 1

    def getValues(self):
        self.conn = Connect()
        self.cr = self.conn.cursor()
        q = "select id,name,description,duration,ingredients,category,user from recipe"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for row in self.table.get_children():
            self.table.delete(row)    #taki refresh krne pr searched row delete ho jaye
        count = 0
        for i in data:
            self.table.insert('', index=count, values=i)
            count += 1

    def getCatName(self):
        conn = Connect()
        cr = conn.cursor()
        q = "select name from category"
        cr.execute(q)
        result = cr.fetchall()
        lst = []
        for i in result:
            lst.append(i[0])
        return lst

    def update(self):
        userid = self.txt7.get()
        id = self.txt1.get()
        name = self.txt2.get()
        description = self.txt3.get('1.0', 'end-1c')
        duration = self.txt4.get()
        ingredients = self.txt5.get()
        category = self.txt6.get()

        q = f"update recipe set name='{name}', description='{description}', duration='{duration}'," \
            f"ingredients='{ingredients}', category='{category}' where id = '{id}'"
        self.cr.execute(q)
        self.conn.commit()
        self.getValues()
        self.root1.destroy() #after update destoy window
        msg.showinfo("SUCCESS", "recipe has been updated", parent=self.root)

    def playText(self):
        lst = os.listdir('.')
        print(lst)

        if 'hello.mp3' in lst:
            os.remove('hello.mp3')

        obj = gTTS(text=self.txt3.get('1.0', 'end-1c'), lang='en')

        obj.save("hello.mp3")

        playsound.playsound('hello.mp3')

        os.remove('hello.mp3')



if __name__ == '__main__':
    object = view()
