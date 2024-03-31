from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect
from tkinter.filedialog import askopenfilename
import cv2
import random


class Main:
    def __init__(self, userID):
        self.root = Tk()
        self.root.geometry("800x800")
        self.root.title("recipe")
        self.root.configure(bg="#AD9BAA")

        self.label = Label(self.root, text="Add Recipe", font=('', 20, 'bold'), bg="#CFCCD6")
        self.label.pack(pady=20, ipadx=10, ipady=10)

        self.formFrame = Frame(self.root, bg="#CFCCD6")
        self.formFrame.pack()
        self.font = ("arial", 14)

        self.lb1 = Label(self.formFrame, text="Name", font=self.font, bg="#CFCCD6")
        self.txt1 = Entry(self.formFrame, font=self.font)
        self.lb1.grid(row=0, column=0, pady=15, padx=10)
        self.txt1.grid(row=0, column=1, pady=15, padx=10)

        self.lb2 = Label(self.formFrame, text="Description", font=self.font, bg="#CFCCD6")
        self.txt2 = Text(self.formFrame, font=self.font, height=5, width=30)
        self.lb2.grid(row=1, column=0, pady=15, padx=10)
        self.txt2.grid(row=1, column=1, pady=15, padx=10)

        self.lb3 = Label(self.formFrame, text="Duration", font=self.font, bg="#CFCCD6")
        self.txt3 = Entry(self.formFrame, font=self.font)
        self.lb3.grid(row=2, column=0, pady=15, padx=10)
        self.txt3.grid(row=2, column=1, pady=15, padx=10)

        self.lb4 = Label(self.formFrame, text="Ingredients", font=self.font, bg="#CFCCD6")
        self.txt4 = Text(self.formFrame, font=self.font,height=3, width=30)
        self.lb4.grid(row=3, column=0, pady=15, padx=10)
        self.txt4.grid(row=3, column=1, pady=15, padx=10)

        self.lb5 = Label(self.formFrame, text="Category", font=self.font, bg="#CFCCD6")
        self.txt5 = ttk.Combobox(self.formFrame, font=self.font, state='readonly', values=self.getCatName())
        self.lb5.grid(row=4, column=0, pady=15, padx=10)
        self.txt5.grid(row=4, column=1, pady=15, padx=10)

        self.lb6 = Label(self.formFrame, text="User ID", font=self.font, bg="#CFCCD6")
        self.txt6 = Entry(self.formFrame, font=self.font)
        self.txt6.insert(0, userID)
        self.txt6.configure(state='readonly')
        self.lb6.grid(row=5, column=0, pady=15, padx=10)
        self.txt6.grid(row=5, column=1, pady=15, padx=10)

        self.lb7 = Label(self.formFrame, text="Select Image", font=self.font, bg="#CFCCD6")
        self.lb7.grid(row=6, column=0, pady=20, padx=20)
        self.txt7 = Entry(self.formFrame, width=30)
        self.txt7.grid(row=6, column=1, pady=20)
        self.btn2 = Button(self.formFrame, text='Select', font=('ariel', 15, 'bold'), command=self.selectImage)
        self.btn2.grid(row=6, column=2, pady=20)

        self.submit = Button(self.root, width=25, text="SUBMIT", font=self.font, command=self.insert)
        self.submit.pack(pady=20)

        self.root.mainloop()

    def selectImage(self):
        imagepath = askopenfilename(filetypes=[('Images', '*.png;*.jpg;*.jpeg')])
        self.txt7.delete(0, 'end')
        self.txt7.insert(0, imagepath)

    def getCatName(self):
        conn = Connect()
        cr = conn.cursor()
        q = "select name from category"
        cr.execute(q)
        result = cr.fetchall()
        lst = []  # converting tuple into list, 2-D into 1-D tuple of tuple mil raha tha usko list mein convert kra
        for i in result:
            lst.append(i[0])
        return lst

    def insert(self):
        name = self.txt1.get()
        description = self.txt2.get('1.0', 'end-1c')
        # print(description)
        duration = self.txt3.get()
        ingredients = self.txt4.get('1.0', 'end-1c')
        category = self.txt5.get()
        user = self.txt6.get()

        if name == '' or description == '' or duration == '' or ingredients == '' or category == '' or user == '':
            msg.showwarning("warning", "please enter all values", parent=self.root)
        else:
            conn = Connect()
            cr = conn.cursor()

            q = f"insert into recipe values(null,'{name}','{description}','{duration}','{ingredients}','{category}'," \
                f"'{user}','')"
            print(q)
            cr.execute(q)
            conn.commit()
            id = cr.lastrowid
        
            file = self.txt7.get()
            img = cv2.imread(file)
            image_name = f"pictures/{id}.png"
            q = f"update recipe set image='{image_name}' where id='{id}'"
            print(q)
            cr.execute(q)
            cv2.imwrite(image_name, img)
            conn.commit()
            msg.showinfo("SUCCESS", "RECIPE HAS BEEN ADDED", parent=self.root)
            self.txt1.delete(0, 'end')
            self.txt3.delete(0, 'end')
            self.txt4.delete('1.0', 'end-1c')
            self.txt5.set('')
            self.txt2.delete('1.0', 'end-1c')
            self.txt6.delete(0, 'end')

if __name__ == '__main__':
    obj = Main()


#pip install opencv-python (to save image)
#while importiing cv2 name